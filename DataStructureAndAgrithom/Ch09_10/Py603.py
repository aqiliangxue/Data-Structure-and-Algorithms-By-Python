
# 树是一种“非线性数据结构”,由节点和边构成，没有子节点的节点称为叶节点
# 实现二叉树，二叉树定义：每个节点最多有两个子节点

# 递归实现二叉树
def BinaryTree(r):
    return [r,[],[]]

# 将新节点插入树中，为其直接的左子节点
def insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t)>0:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
# 将新节点插入树中，为其直接的右子节点
def insertRight(root,newBranch):
    t=root.pop(2)
    # 如果原节点有值，将原节点作为新节点的子节点
    if len(t)>0:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0]=newVal

# 返回左右子树
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__=="__main__":
    r=BinaryTree(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)
    l=getLeftChild(r)
    print(l)

    setRootVal(l,9)
    print(r)

    insertLeft(l,11)
    print(r)
    print(getRightChild(getRightChild(r)))