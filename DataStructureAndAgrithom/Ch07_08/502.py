
# 二分法查找
def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if item < alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found

testList=[0,1,2,8,13,17,19,32,43]
# print(binarySearch(testList,3))
# print(binarySearch(testList,13))

def binarySearch1(alist,item):
    # if len(alist)==0:
    #     return False
    if len(alist)==1:
        return alist[0]==item
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

testList=[0,1,2,8,13,17,19,32,43]
print(binarySearch1(testList,0))
print(binarySearch1(testList,43))




