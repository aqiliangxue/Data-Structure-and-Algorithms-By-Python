
# 优化问题：兑换最少个数的硬币
# 贪心策略：每次试图解决尽量大的一部分，对应到兑换硬币问题，就是每次以最多数量的最大面值来迅速减少找零面值

# 找零兑换问题的递归解法
def recMC(coinValueList,change):
    # 最大问题是及其低效，重复计算太多
    minCoins=change
    if change in coinValueList:
        # 最小规模，直接返回
        return 1
    else:
        # 对每种硬币尝试1次，选择最小的一个
        for i in [c for c in coinValueList if c<=change]:#去掉比找零面值大的硬币
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
    return minCoins

# 改进算法，关键在于消除重复计算，可以用一个表将计算过的中间结果保存起来，在计算之前查看是否已经计算过
# 算法的中间计算结果就是部分找零的最优解，在计算之前，先查找表中是否已有部分找零最优解
# 如果有直接返回，不去做递归调用
def recMC_Adv(coinValueList,change,knowResults):
    minCoins=change
    if change in coinValueList:  #递归结束基本条件
        knowResults[change]=1    #记录最优解
        return 1
    elif knowResults[change]>0:
        return knowResults[change] #查表成功，直接用最优解
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC_Adv(coinValueList,change-i,knowResults)
            if numCoins<minCoins:
                minCoins=numCoins
                # 找到最优解，记录到表中
                knowResults[change]=minCoins
    print(knowResults)
    return minCoins
# knowResults=[]
import time
print(time.perf_counter())
print(recMC_Adv([1,5,10,25],26,[0]*27))
print(time.perf_counter())