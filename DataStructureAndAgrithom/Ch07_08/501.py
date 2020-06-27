

# 顺序查找，无序表查找代码
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

# 顺序查找：有序表查找，当前面数据项不相等，下一数据项又大于要查找数据，对于有序表来说可以确定数据不存在在要查找的表中
def OrderedsequentualSearch(alist,item):
    pos=0
    found=False
    stop=False
    while pos<len(alist) and found==False and stop==False:
        if alist[pos]==item:
            found=True
        else:
            # 增加提前退出条件
            if alist[pos]>item:
                stop=True
            else:
                pos+=1
    return found

testList=[0,1,2,8,13,17,19,32,43]
print(OrderedsequentualSearch(testList,3))
print(OrderedsequentualSearch(testList,13))