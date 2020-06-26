

"""
1、AYL树：平衡二叉查找树，在key插入时一直保持平衡的二叉查找树，实现基本与bst的实现相同，不同之处在于二叉树的生成与维护过程
2、avl的实现中，需要对每个节点跟踪“平衡因子参数”，平衡因子是根据节点的左右子树的高度来定义的，确切的说是左右子树的高度差
    如果平衡因子大于0，称为“左重”，小于0称为“右重”，等于0则称为平衡
3、如果二叉查找树中每个节点的平衡因子都在-1，0，1之间，则吧这个二叉搜索树称为平衡树
4、avl树的搜素时间复杂度为h=1.44log(Nh) h为树深度，Nh为节点总个数
5、作为bst，新key必定以叶节点形式插入到avl树当中
6、叶节点的平衡因子是0，本身无需重新平衡，但会影响父节点的平衡因子，插入左子节点平衡因子加1，插入有子节点，平衡因子减1
    这种影响随着其父节点到根节点的路径一直传递上去，直到 传递到根节点为止，或者某个父节点平衡因子被调整到0，不在影响上层节点的平衡因子为止

"""

# 基本与bst的实现相同,只是重新定义其中一些方法
def _put(self, key, val, currentNode):
    # 重新定义_put方法
    # 如果key比currentNode小，那么_put到左子树
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key, val, currentNode.leftChild)
        else:
            # 如果没有左子树，那么key就成为左子节点，同时也是递归结束条件
            currentNode.leftChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.leftChild)

    else:
        # 如果key比currentNode大，那么_put到右子树
        if currentNode.hasRightChild():
            self._put(key, val, currentNode.rightChild)
        else:
            # 如果没有右子树，那么key就成为右子节点，同时也是递归结束条件
            currentNode.rightChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNode.rightChild)

def updateBalance(self,node):
    if node.balanceFactor >1 or node.balanceFactor < -1:
        # 重新平衡
        self.rebalance(node)
        return
    if node.parent != None:
        if node.isLeftChild():
            node.parent.balanceFactor+=1
        elif node.isRightChild():
            node.parent.balanceFactor-=1

        if node.parent.balanceFactor!=0:
            # 调整父节点因子，直到上层父节点为0，不会再往上一层产生影响
            self.updateBalance(node.parent)

# rebalance 重新平衡，将不平衡的子树进行旋转，视左重或者右重进行不同方向的旋转，同时更新相关父节点引用，更新旋转后被影响节点的平衡因子

def rotateLeft(self,rotRoot):
    # 设定新的根节点
    newRoot=rotRoot.rightChild
    # 将新根节点的左子节点挂到挂到旧根的右子节点
    rotRoot.rightChild=newRoot.leftChild
    # 更新父节点指向
    if newRoot.leftChild!=None:
        newRoot.leftChild.parent=rotRoot
    newRoot.parent=rotRoot.parent
    if rotRoot.isRoot():
        self.root=newRoot
    else:
        if rotRoot.isLeftChild():
            rotRoot.parent.leftChild=newRoot
        else:
            rotRoot.parent.rightChild=newRoot
    newRoot.leftChild=rotRoot
    rotRoot.parent=newRoot
    # 仅有两个节点需要调整因子
    rotRoot.balanceFactor=rotRoot.balanceFactor+1-min(newRoot.balanceFactor,0)
    newRoot.balanceFactor=newRoot.balanceFactor+1+max(rotRoot.balanceFactor,0)


def rebalance(self,node):
    # 右重需要左旋
    if node.balanceFactor<0:
        if node.rightChild.balanceFactor>0:
            # 右子节点左重先右旋
            self.rotateRight(node.rightChild)
            self.rotateLeft(node)
        else:
            self.rotateLeft(node)
    # 左重需要右旋
    elif node.balanceFactor>0:
        if node.leftChild.balanceFactor<0:
            # 左子节点右重先左旋
            self.rotateLeft(node.leftChild)
            self.rotateRight(node)
        else:
            self.rotateRight(node)

















