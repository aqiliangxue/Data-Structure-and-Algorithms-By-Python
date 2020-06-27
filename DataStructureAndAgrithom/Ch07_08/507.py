
"""
快速排序：依据一个“中值”数据来吧数据表分为两半，小于中值的一半，和大于中值的一半，然后每部分分别进行快速排序（递归）
基本结束条件：数据表仅有一个数据项，自然是排好序的
缩小规模：根据中值，将数据表分为两半，最好情况是相等的两半
调用自身：将两半分别调用自身进行排序
# 运行中不需要额外的存储空间，关键点是中值的选取，选取不合适复杂度退化到O（n*n）

分裂数据表手段：
1、设置左右标
2、坐标向右移动，右标向左移动
    坐标一直向右移动，碰到比中值大的就停止
    右标向左移动，碰到比中值小的就停止
    然后把左右标指向的数据交换
3、继续移动，直到坐标移动到右标的右侧，停止移动，这时右标所指的位置就是“中值”应处的位置，将中值和这个位置交换
4、分裂完成，左半部比中值小，右半部比中值大
"""

def partion(alist,first,last):
    pivotvalue=alist[first]

    leftmark=first+1
    rightmark=last

    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            # 如果坐标指向数据小于中值，坐标加1
            leftmark=leftmark+1

        while alist[rightmark]>=pivotvalue and rightmark>=leftmark:
            # 如果右标指向数据大于中值，右标减1
            rightmark=rightmark-1

        if rightmark< leftmark:
            done=True
        else:
            # 将坐标指向数据大于中值，右标指向数据小于中值数据项交换
            tmp=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=tmp
    # 右标移动到坐标左侧，此时右标位置就是“中值“应处位置，将中值和这个位置交换
    tmp=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=tmp

    return rightmark

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitPoint=partion(alist,first,last)
        quickSortHelper(alist,first,splitPoint-1)
        quickSortHelper(alist,splitPoint+1,last)

alist=[54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
