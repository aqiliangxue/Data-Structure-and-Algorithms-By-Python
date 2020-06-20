
class Binheap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0

    def percUp(self,i):
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
        self.percDown(1)

        return retVal

    def buildHeap(self,alist):
        # 从最后节点父节点开始下沉，因叶节点无需下沉
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








