def sequentualSearch(alist,item):
    pos=0
    found=False
    while pos<len(alist) and found==False:
        if alist[pos]==item:
            found=True
        else:
            pos+=1
    return found

# testList=[1,2,32,8,17,19,42,13,0]
# print(sequentualSearch(testList,3))
# print(sequentualSearch(testList,13))

def OrderedsequentualSearch(alist,item):
    pos=0
    found=False
    stop=False
    while pos<len(alist) and found==False and stop==False:
        if alist[pos]==item:
            found=True
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos+=1
    return found

testList=[0,1,2,8,13,17,19,32,43]
print(OrderedsequentualSearch(testList,3))
print(OrderedsequentualSearch(testList,13))