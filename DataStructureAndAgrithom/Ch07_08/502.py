
# 二分法查找，体现了解决问题的策略：分而治之，将问题分为若干规模更小的部分，算法复杂度为O（log n）
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

# 二分查找的递归算法版本
def binarySearch1(alist,item):
    # if len(alist)==0:
    #     return False
    if len(alist)==1:
        # 结束条件
        return alist[0]==item
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                # 缩小规模，调用自身，切片操作复杂度为O（k）
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)

testList=[0,1,2,8,13,17,19,32,43]
print(binarySearch1(testList,0))
print(binarySearch1(testList,43))




