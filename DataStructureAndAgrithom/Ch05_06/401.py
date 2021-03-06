
"""
递归三定律：
1、递归算法必须有一个基本结束条件（最小规模问题的直接解决）
2、递归算法必须能够改变状态向基本结束条件演进（减小问题规模）
3、递归算法必须调用自身（解决减小了规模的相同问题）

"""

def listnum(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        return numlist[0]+listnum(numlist[1:])

def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)

def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]


# def tellstory():
#     print("从前有座山，山里有个庙，庙里有个老和尚，老和尚在讲一个故事,讲什么呢，在讲：")
#     tellstory()


if __name__=="__main__":
    # print(listnum([1,2,3,4]))
    # print(jiecheng(5))
    # print(toStr(16385,16))
    print(16385%16)

    # 获得递归最大深度
    # import sys
    # print(sys.getrecursionlimit())
    # tellstory()