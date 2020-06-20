from basis.Deque import Deque

def palChecker(aString):
    charDeque=Deque()
    for ch in aString:
        charDeque.addRear(ch)
    stillEqual=True
    while charDeque.size()>1 and stillEqual:
        first=charDeque.removeFront()
        second=charDeque.removeRear()
        if first!=second:
            stillEqual=False
    return stillEqual

print(palChecker("lsdkjfsk"))
print(palChecker("radar"))
