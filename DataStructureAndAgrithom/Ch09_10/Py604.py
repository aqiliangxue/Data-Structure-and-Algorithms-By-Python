
# 通过节点链接法实现树
class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        # 成员leftChild&rightChild 保存指向左右子树的引用（也是BinaryTree对象）
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild=BinaryTree(newNode)
        else:
            # 需要注意赋值步骤，顺序错了会破坏二叉树
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self,obj):
        self.key=obj

    def getRootValue(self):
        return self.key

    def preOrder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()


if __name__=="__main__":
    r=BinaryTree("a")
    r.insertLeft("b")
    r.insertRight("c")
    r.getRightChild().setRootValue("hello")
    r.getLeftChild().insertRight("d")

    print(r.preOrder())