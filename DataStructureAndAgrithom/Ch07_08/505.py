
# 谢尔排序：以插入排序为基础，对无序表进行“间隔”划分子列表，每个子列表进行插入排序，复杂度介于n和n*n之间
def shellSort(alist):
    # 间隔设定，间隔越来越小，则子列表数量越来越少，无序表的整体越来越有序，从而减小整体比对次数
    sublistcount=len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            # 子列表排序
            gapInsertionSort(alist,startposition,sublistcount)
        print("After increments of size",sublistcount,"The list is ",alist)
        # 间隔缩小
        sublistcount=sublistcount//2
    return alist

def gapInsertionSort(alist,start,gap):
    # 参考插入排序对比即可
    for i in range(start+gap,len(alist),gap):
        currentvalue=alist[i]
        position=i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position=position-gap
        alist[position]=currentvalue

alist=[54,26,93,17,77,31,44,55,20]
print(shellSort(alist))


