
"""
二叉查找树bst，比父节点小的key，都出现在左子树，比父节点大的key，都出现在右子树
数据插入顺序不同，生成的bst也不同

"""
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        # 直接调用了TreeNode中的同名方法
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            # 递归函数
            self._put(key, val, self.root)
        else:
            # 如果bst为空，那么key成为根节点root
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):

        # 如果key比currentNode小，那么_put到左子树
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                # 如果没有左子树，那么key就成为左子节点，同时也是递归结束条件
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            # 如果key比currentNode大，那么_put到右子树
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                # 如果没有右子树，那么key就成为右子节点，同时也是递归结束条件
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, value):
        # 特殊方法实现索引赋值，可以使用 myTree[6] = "yellow"格式
        self.put(key, value)

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def __getitem__(self, key):
        # 特殊方法实现索引取值 val = myTree[6]
        return self.get(key)

    def __contains__(self, key):
        #  3 in myTree
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError("Error ,key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error , tree not in tree")

    def __delitem__(self, key):
        # 特殊方法实现 del myTree[6] 这样的语句操作
        self.delete(key)

    def remove(self, currentNode):
        """
        分三种情况：
            1、这个节点没有子节点
            2、这个节点有1个子节点
            3、这个节点有2个子节点
        :param currentNode:
        :return:
        """
        if currentNode.isLeaf():
            # 是叶子节点直接删除即可
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():
            # 有两个子节点，为节点找后继，这个合适节点就是被删节点右子树中最小的那个，称为”后继"
            succ=currentNode.findSuccessor()

            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.payload=succ.payload

        else:  # 这个节点有一个子节点
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    # 根节点删除，相当于把根节点数据替换为子节点数据
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChilld
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replceNodeData(currentNode.rightChild.key,
                                               currentNode.rightChild.payload,
                                               currentNode.rightChild.leftChild,
                                               currentNode.rightChild.rightChilld)





class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild and self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        # 如果有左右子节点，则左右子节点指向的父节点也需要更新
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        # 中序遍历的迭代
        if self:
            if self.hasLeftChild():
                # 实际上是递归函数
                for elem in self.leftChild:
                    yield elem
            yield self.key

            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def findSuccessor(self):
        succ=None
        if self.hasRightchild():
            # 找到右子树中最小的节点
            succ=self.rightChild.findMin()
        else:
            # 目前不会遇到，代码前提是有左右子节点情况下
            if self.parent:
                if self.isLeftChild():
                    succ=self.parent
                else:
                    self.parent.rightChild=None
                    succ=self.parent.findSuccessor()
                    succ.parent.rightChild=self
        return succ

    def findMin(self):
        current=self
        while current.hasLeftChild():
            current=current.leftChild
        return current

    def spliceOut(self):
        # 将节点摘除
        if self.isLeaf():
            # 只有叶子节点，直接摘除
            if self.isLeftChild():
                self.parent.leftChild=None
            else:
                # 不会被执行
                self.parent.rightChild=None
        elif self.hasAnyChildren():
            if self.hasLeftChildren():
            # 目前不会遇到，因为执行findmin后不会再有左子节点
                if self.isLeftChild():
                    self.parent.leftChlild=self.leftChild
                else:
                    self.parent.rightChild=self.leftChild
                self.leftChild.parent=self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild=self.rightChild
                else:
                    # 不会被执行
                    self.parent.rightChild=self.rightChild
                self.rightChild.parent=self.parent


if __name__ == "__main__":
    myTree = BinarySearchTree()
    myTree[3] = "red"
    myTree[4] = "blue"
    myTree[6] = "yellow"

    print(myTree[3])
    print(3 in myTree)
    for i in myTree:
        print(i, myTree[i])
