from Ch11_12.Py703 import  Graph

filePath="C:\\Users\\zwk\\PycharmProjects\\DataStructureAndAgrithom\\fourletterwords.txt"

def BuildGraph(filePath):
    d={}
    g=Graph()
    wfile=open(filePath,'r')
    for line in wfile:
        word=line[:-1]
        for i in range(len(word)):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
    # print(d)
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    return g














