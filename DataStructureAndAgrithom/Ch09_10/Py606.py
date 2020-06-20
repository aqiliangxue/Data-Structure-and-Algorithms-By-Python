from basis.Stack import Stack
from Ch09_10.Py604 import BinaryTree
import operator

def buildParseTree(fpexp):
    fplist=fpexp.split()
    # print(fplist)
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i=='(':
            # print("(")
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            # print("num")
            currentTree.setRootValue(int(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in ['+','-','*','/'] :
            # print("op")
            currentTree.setRootValue(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
        elif i ==')':
            currentTree=pStack.pop()
            # print(")")
        else:
            raise ValueError

    return eTree

def evaluate(parseTree):
    opers= {"+":operator.add,"-":operator.sub, \
            "*":operator.mul,"/":operator.truediv}

    leftC=parseTree.getLeftChild()
    RightC=parseTree.getRightChild()

    if leftC and RightC:
        fn=opers[parseTree.getRootValue()]
        return fn(evaluate(leftC),evaluate(RightC))
    else:
        return parseTree.getRootValue()


if __name__=="__main__":

    test=buildParseTree("( 3 + ( 4 * 5 ) )")
    # print(test)
    # print(evaluate(test))
    test.preOrder()


