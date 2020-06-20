from Ch09_10.Py606 import buildParseTree
import operator

# 树的遍历
# 前序遍历
def preOrder(tree):
    if tree:
        print(tree.getRootValue())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())
# 后序遍历
def postOrder(tree):
    if tree:

        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootValue())
# 中序遍历
def inOrder(tree):
    if tree:

        inOrder(tree.getLeftChild())
        print(tree.getRootValue())
        inOrder(tree.getRightChild())
# 后序遍历应用
def postOrdereval(tree):
    opers = {"+": operator.add, "-": operator.sub, \
             "*": operator.mul, "/": operator.truediv}

    res1=None
    res2=None
    if tree:
        res1=postOrdereval(tree.getLeftChild())
        res2=postOrdereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootValue()](res1,res2)
        else:
            return tree.getRootValue()

# 中序遍历应用
def printexp(tree):
    sVal=""
    if tree:
        # sVal='('+printexp(tree.getLeftChild())
        # sVal=sVal+str(tree.getRootValue())
        # sVal=sVal+printexp(tree.getRightChild())+')'

        if tree.getLeftChild()!=None:
            sVal = '(' + printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootValue())
        if tree.getRightChild()!=None:
            sVal=sVal+printexp(tree.getRightChild())+')'
    return sVal

if __name__=="__main__":

    test=buildParseTree("( 3 + ( 6 * 5 ) )")
    # preOrder(test)
    # print("\n")
    # postOrder(test)
    # print("\n")
    # inOrder(test)
    # print("\n")
    # print(postOrdereval(test))
    print(printexp(test))
