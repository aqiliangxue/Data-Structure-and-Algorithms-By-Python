from Ch11_12.Py703 import  Graph

filePath="C:\\Users\\zwk\\PycharmProjects\\DataStructureAndAgrithom\\fourletterwords.txt"
# 词梯问题是无向边，边没有权重
def BuildGraph(filePath):
    d={}
    g=Graph()
    wfile=open(filePath,'r')
    for line in wfile:
        # 得到该行单词
        word=line[:-1]
        # print(word)
        for i in range(len(word)):
            # 分桶，每个桶内单词只差一个字母
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
    # print(d)
    # 为同一个桶内的单词添加边，每个桶内单词只差一个字母
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    # 最后得到单词关系图是一个稀疏图
    return g


# a=[1,2,3]
# print(a[:-1])











