from basis.Stack import Stack
from Ch09_10.Py604 import BinaryTree
import operator

# 树的应用，解析树（语法树）
# 表达式解析： 叶节点保存操作数，内部节点保存操作符
def buildParseTree(fpexp):
    """
    从全括号表达式构建表达式解析树
    以( 3 + ( 4 * 5 ) )为例
    1、创建空树，当前节点为根节点
    2、读入（，创建左子节点，当前节点下降
    3、读入3，当前节点设置为3，上升到父节点
    4、读入+，当前节点设置为+，创建右子节点，当前节点下降
    5、读入（，创建左子节点，当前节点下降
    6、读入4，当前节点设置为4，上升到父节点
    7、读入*，当前节点设置为*，创建右子节点，当前节点下降
    8、读入5，当前节点设置为5，上升到父节点
    9、读入），上升到父节点
    10、读入），再上升到父节点
    上升到父节点没有方法支持，引入栈来记录跟踪父节点，当前节点下降时，将下降前的节点push入栈，当前节点需要上升到父节点时，上升到pop出栈的节点即可
    """


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

# 表达式求值
"""
递归三要素：
    1、基本结束条件：叶节点是最简单子树，没有子节点，其根节点的数据项即为子表达式的值
    2、缩小规模：将表达式树分解为左子树、右子树，即缩小规模
    3、调用自身：分别调用evaluate计算左子树、右子树的值，然后将左右子树的值依据根节点的操作符进行计算，从而得到表达式的值   
"""

def evaluate(parseTree):
    opers= {"+":operator.add,"-":operator.sub, \
            "*":operator.mul,"/":operator.truediv}
    # 缩小规模
    leftC=parseTree.getLeftChild()
    RightC=parseTree.getRightChild()

    if leftC and RightC:
        fn=opers[parseTree.getRootValue()]
        # 递归调用
        return fn(evaluate(leftC),evaluate(RightC))
    else:
        # 基本结束条件
        return parseTree.getRootValue()


if __name__=="__main__":

    test=buildParseTree("( 3 + ( 4 * 5 ) )")
    # print(test)
    # print(evaluate(test))
    test.preOrder()


