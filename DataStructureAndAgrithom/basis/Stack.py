# -*- encoding=utf-8 _*_
class Stack:
    def __init__(self):
        self.iterms=[]

    def isEmpty(self):
        return self.iterms==[]

    def push(self,item):
        self.iterms.append(item)

    def pop(self):
        return self.iterms.pop()

    def peek(self):
        return self.iterms[len(self.iterms)-1]

    def size(self):
        return len(self.iterms)

# if __name__=="__main__":
#     a=Stack()
#     a.push("wo")
#     a.push("shi")
#     a.push("zhou wei ke")
#     b=a.pop()
#     print(b)
#     print(a.peek())


    # print(a.size())