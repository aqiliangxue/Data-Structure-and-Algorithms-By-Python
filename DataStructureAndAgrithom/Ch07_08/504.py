

# 插入排序，时间复杂度仍然为O（n*n），维持一个已经排序好的子列表，其位置始终在列表的前部，然后逐步扩大到整个列表
# 列表越接近有序，插入排序的比对次数就越少
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue=alist[index]
        # 该索引包含的数据已经取出，将position指向该index
        position=index
        while position>0 and alist[position-1]>currentValue:
            alist[position]=alist[position-1]
            position-=1
        alist[position]=currentValue
    return alist

alist=[54,26,93,17,77,31,44,55,20]
print(insertionSort(alist))
