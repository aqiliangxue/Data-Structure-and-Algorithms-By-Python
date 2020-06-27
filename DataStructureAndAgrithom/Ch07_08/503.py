
# 冒泡排序，需要比较n-1趟
def bubbleSort(alist):
    # n-1躺比较，len(alist)-1,0,-1，从n-1到1，不包括0
    for passnum in range(len(alist)-1,0,-1):
        # print(passnum)
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                # python支持直接交换
                alist[i],alist[i+1]=alist[i+1],alist[i]
    return alist
# alist=[54,26,93,17,77,31,44,55,20]
# b=bubbleSort(alist)
# print(b)
# c=[i for i in range(0,8)]
# print(c)

# 改进算法，如果某趟对比没有发生任何交换，说明列表已经排好序，可以提前退出
def shortBubbleSort(alist):
    exchange=True
    passnum=len(alist)-1
    while passnum >0 and exchange==True:
        exchange=False
        # print(passnum)
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                # 本趟对比需要发生交换，将exchange设置为true
                exchange = True
                alist[i],alist[i+1]=alist[i+1],alist[i]
        passnum-=1
    return alist
# alist=[54,26,93,17,77,31,44,55,20]
# b=shortBubbleSort(alist)
# print(b)

# 选择排序，每趟比对记录最大项的位置，每趟只做一次交换
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax=location
        temp=alist[fillslot]
        alist[fillslot]=alist[positionOfMax]
        alist[positionOfMax]=temp
    return alist

alist=[54,26,93,17,77,31,44,55,20]
b=selectionSort(alist)
print(b)
# d=[i for i in range(1,5)]
# e=[j for j in range(4)]
# print(d)
# print(e)
