from basis.Stack import Stack

# a=Stack()
# a.push("test")
# print(a.peek())
def parChecker(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty()==True:
                balanced=False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def parCheckerAdv(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol in"({[":
            s.push(symbol)
        else:
            if s.isEmpty()==True:
                balanced=False
            else:
                # s.pop()
                top=s.pop()
                if not matches(top,symbol):
                    balanced=False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens="([{"
    closes=")]}"
    return opens.index(open)==closes.index(close)



if __name__=="__main__":
    # print(parChecker("((()))"))
    # a=["1","2","3"]
    # print(a.index("2"))
    print(parCheckerAdv("{[()]}"))
