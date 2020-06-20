class Node:
    def __init__(self,initData):
        self.data=initData
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,NewData):
        self.data=NewData

    def setNext(self,newnext):
        self.next=newnext
# tmp=Node(93)
# print(tmp.getdata())

class UnorderedList:
    def __init__(self):
        self.head=None

    def add(self,item):
        temp=Node(item)
        # 下面两行调用次序非常重要，必须注重顺序
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.getNext()
        return count

    def search(self,item):
        current=self.head
        found=False
        while current!= None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found

    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
                if current==None:
                    return "Data Not exist"
        if previous==None:
            self.head=current.getNext()
            return "Succeed,Found data in head"
        else:
            previous.setNext(current.getNext())
            return "Succeed,Found data in middle"

class OrderedList:
    def __init__(self):
        self.head=None
    def search(self,item):
        current=self.head
        found=False
        stop=False
        while current!=None and not found and not stop:
            if current.getData()==item:
                found=True
            else:
                if current.getData()>item:
                    stop=True
                else:
                    current=current.getNext()
        return found

    def add(self,item):
        current=self.head
        previous=None
        stop=False
        while current!=None and not stop:
            if current.getData()>item:
                stop=True
            else:
                previous=current
                current=current.getNext()
        tmp=Node(item)
        if previous==None:
            tmp.setNext(self.head)
            self.head=tmp
        else:
            tmp.setNext(current)
            previous.setNext(tmp)

    def size(self):
            count = 0
            current = self.head
            while current != None:
                count += 1
                current = current.getNext()
            return count

    def search(self, item):
            current = self.head
            found = False
            while current != None and not found:
                if current.getData() == item:
                    found = True
                else:
                    current = current.getNext()
            return found

    def remove(self, item):
            current = self.head
            previous = None
            found = False
            while current != None and not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    # if current == None:
                    #     return "Data Not exist"
            if previous == None:
                self.head = current.getNext()
                # return "Succeed,Found data in head"
            else:
                previous.setNext(current.getNext())
                # return "Succeed,Found data in middle"


if __name__=="__main__":
    # a=UnorderedList()
    a=OrderedList()
    a.add("1")
    a.add("2")
    a.add("3")
    print(a.size())
    # print(a.search("2"))
    # print(a.remove("3"))
    print(a.search("1"))
    print(a.search("2"))
    print(a.search("3"))
    print(a.remove("3"))
    print(a.size())