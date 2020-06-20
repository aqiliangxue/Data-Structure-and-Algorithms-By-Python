
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

def mergeSort1(lst):
    if len(lst)<=1:
        return lst
    middle=len(lst)//2
    left=mergeSort1(lst[:middle])
    right=mergeSort1(lst[middle:])

    merge=[]
    while left and right:
        if left[0]<=right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    merge.extend(right if right else left)
    return merge

# print(mergeSort1(alist))
