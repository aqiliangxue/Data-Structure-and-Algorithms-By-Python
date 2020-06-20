




def dpMakeChange(coinValueList,change,minCoins):
    for cents in range(1,change+1):
        # 初始化一个最大值
        coinCount=cents
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
        minCoins[cents]=coinCount
    return minCoins[change]

def dpMakeChange1(coinValueList,change,minCoins,coinsUsed):
    for cents in range(1,change+1):
        # 初始化一个最大值
        newCoin=1
        coinCount=cents
        for j in [c for c in coinValueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        minCoins[cents]=coinCount
        coinsUsed[cents]=newCoin
    return minCoins[change]

def printCoin(coinsUsed,change):
    coin=change
    while coin>0:
        thisCoin=coinsUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin

print(dpMakeChange([1,5,10,21,25],99,[0]*100))

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