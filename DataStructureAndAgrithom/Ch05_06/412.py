
# 动态规划：背包问题，博物馆大盗问题
# m[(i,w)]，前i（1<=i<=5)个宝物中，组合不超过W（1<=W<=20)重量，得到的最大价值
# m[(i,w)]应该是m[(i-1,w)]和m[(i-1,W-Wi)]+Vi两者的最大值
def dynamic():
    # 宝物的重量和价值
    tr=[None,{"w":2,"v":3},{"w":3,"v":4},{"w":4,"v":8},{"w":5,"v":8},{"w":9,"v":10}]
    # 大盗最大承重
    max_w=20
    # 初始化二维表格m[(i,w)]
    # 表示前i个宝物中，最大重量w的组合，所得到的最大价值
    # 当i什么都不取，或w上限为0，价值均为0
    m={(i,w):0 for i in range(len(tr)) for w in range((max_w+1))}
    # 逐个填写二维表格
    for i in range(1,len(tr)):
        for w in range(1,max_w+1):
            if tr[i]["w"]>w:#装不下第i个宝物
                m[(i,w)]=m[(i-1,w)]#不装第i个宝物
            else:
                #不装第i个宝物，装第i个宝物，两种情况下的最大值
                m[(i,w)]=max(m[(i,w)],m[(i-1,w-tr[i]["w"])]+tr[i]["v"])

    print(m[(len(tr)-1),max_w])

# 宝物的重量和价值
tr={(2,3),(3,4),(4,8),(5,8),(9,10)}
# 大盗最大承重
max_w=20
# 初始化记忆表格m，key是（宝物组合，最大重量），value是最大价值
m={}
# 递归方法解决博物馆大盗问题
def thief(tr,w):
    if tr==set() or w==0:
        m[(tuple(tr)),w]=0 #tuple是key的要求
        return 0
    elif (tuple(tr),w) in m:
        # print(tuple(tr),w)
        return m[(tuple(tr),w)]
    else:
        vmax=0
        for t in tr:
            # print(t)
            if t[0]<=w:
                #逐个从集合中去掉某个宝物，递归调用
                # 选出所有价值中的最大值
                v=thief(tr-{t},w-t[0])+t[1]
                vmax=max(vmax,v)
        m[(tuple(tr),w)]=vmax
        # print((tuple(tr),w,"s"+str(vmax)))
        print(m[(tuple(tr),w)])
        # print(m,vmax)
        return vmax
print(thief(tr,max_w))
# print(tr==set())
# tr1={}
# print(tuple(tr1))















# dynamic()