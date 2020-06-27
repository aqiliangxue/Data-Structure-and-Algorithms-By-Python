
# 动态规划解法
"""
动态规划算法采用了一种更加有条理的方式得到问题的解
找零兑换的动态规划算法从最简单的1分钱找零的最优解开始，逐步递加上去，直到我们需要的零钱数
在找零递加的过程中，设法保持每一分钱的递加都是最优解，一直加到求解找零钱数，自然得到最优解
问题的最优解包含了更小规模子问题的最优解，这是最优化问题能够用动态规划策略解决的必要条件。
"""

# 找零问题的动态规划算法代码
# 动态规划最主要思想，其每一步依靠以前的最优解得到本步骤的最优解
def dpMakeChange(coinValueList,change,minCoins):
    # 从1分钱开始到change逐个计算最少硬币数
    for cents in range(1,change+1):
        # 初始化一个最大值
        coinCount=cents
        # 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
        # 得到当前最少硬币数，记录到表中
        minCoins[cents]=coinCount
    # 循环结束，得到最优解
    return minCoins[change]

#追溯每一步所用的硬币
def dpMakeChange1(coinValueList,change,minCoins,coinsUsed):
    for cents in range(1,change+1):
        # 初始化一下新加硬币
        newCoin=1
        # 初始化一个最大值
        coinCount=cents
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j #对应的最少数量，所减的硬币
        minCoins[cents]=coinCount
        coinsUsed[cents]=newCoin#记录本步骤家的一个硬币
    return minCoins[change]

def printCoin(coinsUsed,change):
    coin=change
    while coin>0:
        thisCoin=coinsUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin

# print(dpMakeChange([1,5,10,21,25],99,[0]*100))

amnt=63
clist=[1,5,10,21,25]
coinsUsed=[0]*(amnt+1)
coinCount=[0]*(amnt+1)
print("Making change for",amnt,"requires")
print(dpMakeChange1(clist,amnt,coinCount,coinsUsed),"coins")
print("they are")
printCoin(coinsUsed,amnt)
print("the used list as follows:")
print(coinsUsed)