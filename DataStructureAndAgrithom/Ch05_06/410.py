
def recMC(coinValueList,change):
    minCoins=change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC(coinValueList,change-i)
            if numCoins<minCoins:
                minCoins=numCoins
    return minCoins

def recMC_Adv(coinValueList,change,knowResults):
    minCoins=change
    if change in coinValueList:
        knowResults[change]=1
        return 1
    elif knowResults[change]>0:
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c<=change]:
            numCoins=1+recMC_Adv(coinValueList,change-i,knowResults)
            if numCoins<minCoins:
                minCoins=numCoins
                knowResults[change]=minCoins
    print(knowResults)
    return minCoins
# knowResults=[]
import time
print(time.perf_counter())
print(recMC_Adv([1,5,10,25],26,[0]*27))
print(time.perf_counter())