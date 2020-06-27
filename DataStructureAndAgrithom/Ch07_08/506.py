
# 归并排序，分治策略在排序中应用，归并排序是递归算法，思路是将数据表持续分裂为2半，对两半分别进行归并排序
"""
递归的基本结束条件：数据表仅有一个数据项，自然是排好序的
缩小规模：将数据表分裂为相等的两半，规模减小为原来的二分之一
调用自身：将两半分别调用自身排序，然后将分别排好序的两半进行归并，得到排序好的数据表
算法复杂度：O（n*log n）
"""
def mergeSort(alist):
    # 基本结束条件
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        # 递归调用
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        # 拉链式交错吧左右半部从小到大归并到结果列表中 1 2 3 4 5 6
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        # 归并左半部剩余项
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        # 归并右半部剩余项
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
        return alist

alist=[54,26,93,17,77,31,44,55,20]
print(mergeSort(alist))

# 更加python风格的归并排序
def mergeSort1(lst):
    # 递归结束条件
    if len(lst)<=1:
        return lst
    # 分解问题，并递归调用
    middle=len(lst)//2
    # 左半部排好序
    left=mergeSort1(lst[:middle])
    # 右半部排好序
    right=mergeSort1(lst[middle:])
    # 合并左右半部，完成排序
    # 使用额外一倍存储空间用于归并
    merge=[]
    while left and right:
        if left[0]<=right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    #剩余项合并到列表末尾
    merge.extend(right if right else left)
    return merge

# print(mergeSort1(alist))
