from basis.Stack import Stack

def divideBy2(number):
    remStack=Stack()
    while number>0:
        rem=number%2
        remStack.push(rem)
        number=number//2

    binString=""
    while not remStack.isEmpty():
        binString=binString+str(remStack.pop())
    return binString

def baseConverter(number,base):
    remStack=Stack()
    digits="0123456789ABCDEF"
    while number>0:
        rem=number%base
        remStack.push(rem)
        number=number//base

    binString=""
    while not remStack.isEmpty():
        binString=binString+digits[remStack.pop()]
    return binString

if __name__=="__main__":
    # print(divideBy2(1023))
    print(baseConverter(255,16))
    print(baseConverter(16, 8))