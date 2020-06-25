

# 优先队列，高优先级的数据项排在队首，低优先级的数据项排在后面
# 实现优先队列的经典方案是采用二叉堆（采用非嵌套的列表来实现）数据结构，二叉堆能够将优先队列的出队和入队的复杂度都保持在O（log n）
"""
完全二叉树：如果节点下标为p，其左子节点下标为2p，右子节点下标为2p+1，父节点下标为p//2
任何一个节点x，其父节点p中的值，均小于x中的值，根节点中的值最小
"""
class Binheap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0

    def percUp(self,i):
        # 上浮操作，和父节点作比较，如果比父节点小，和父节点的值进行交换，每次//2得到父节点下标
        while i//2>0:
            # i//2 对2整除的到父节点下标,如果子节点小于父节点，互换
            if self.heapList[i]<self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2

    def insert(self,k):
        # 新添加的key放在列表末尾，然后上浮
        self.heapList.append(k)
        self.currentSize=self.currentSize+1
        self.percUp(self.currentSize)

    def percDown(self,i):
        # 下沉操作， 将新的根节点沿着一条路径下沉，直到比2个子节点都小
        # 下沉路径选择，如果比子节点大，选择较小的子节点下沉
        while (i*2)<=self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]>self.heapList[mc]:
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc

    def minChild(self,i):
        # 选择比较小的子节点，交换下沉
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retVal=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.heapList.pop()
        # 新顶下沉
        self.percDown(1)

        return retVal

    def buildHeap(self,alist):
        # 从最后节点父节点开始下沉，因叶节点无需下沉
        # 用下沉法将建堆总代价控制在O（n）
        i=len(alist)//2
        self.currentSize=len(alist)
        self.heapList=[0]+alist[:]
        print(len(self.heapList),i)
        while i>0:
            print(self.heapList,i)
            self.percDown(i)
            i=i-1
        print(self.heapList,i)


a=[12,6,35,79,3,10,20]
c=Binheap()
c.buildHeap(a)

"""
           3
    6           10
79    12    35      20
"""








