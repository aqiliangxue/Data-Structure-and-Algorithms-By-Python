# -*- encoding=utf-8 -*-
from basis.Stack import Stack


def infixToPostfix(infixexpr):
    opNum="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    opNum1="0123456789"
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    opStack=Stack()
    # 后缀表达式列表
    postfixList=[]
    # 以空格拆分
    tokenList=infixexpr.split()
    # print(tokenList)
    for token in tokenList:
        if token in opNum or token in opNum1:
            postfixList.append(token)
        elif token=="(":
            opStack.push(token)
        elif token==")":
            toptoken=opStack.pop()
            while toptoken!="(":
                postfixList.append(toptoken)
                toptoken=opStack.pop()
        else:
            while(not opStack.isEmpty()) and \
                    (prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postfixexpr):
    operandStack=Stack()
    tokenList=postfixexpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(token)
        else:
            operand2=int(operandStack.pop())
            # print(operand2)
            operand1=int(operandStack.pop())
            # print(operand1)
            result=doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()



def doMath(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op=="/":
        return op1/op2
    elif op=="+":
        return op1+op2
    else:
        return op1-op2


if __name__=="__main__":
    # print(infixToPostfix("A + ( B * C )"))
    # (7*6)/7-8
    print(postfixEval("4 5 6 * - "))
