from Ch11_12.Py704 import BuildGraph
from basis.Queue import Queue

def bfs(g,start):
    # 广度优先算法，搜索所有从起始顶点start可到达的边，在搜索更远距离k+1的顶点之前，会搜索完全部距离为k的顶点
    # 算法复杂度为O（v+e）v为顶点数量，e为边的数量
    start.setDistance(0)
    start.setPred=None
    vertQueue=Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        # 取队首为当前顶点
        currentVert=vertQueue.dequeue()
        # 边最多检查一次
        for nbr in currentVert.getConnections():
            # Color 白色：顶点尚未发现，灰色：已经发现，黑色：完成探索
            if (nbr.getColor()=="white"):
                nbr.setColor("gray")
                # 当前节点到起始顶点的距离
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                # 将发现的顶点加入到队列中
                vertQueue.enqueue(nbr)
        # 遍历完后，将当前顶点标记为黑色，标志完成探索
        currentVert.setColor("black")

def traverse(y):
    # 通过回溯函数，得到从开始顶点start到任何单词的最短词梯
    # getPred()获取前驱顶点
    x=y
    while (x.getPred()):
        print(x.getId())
        x=x.getPred()
    print(x.getId())


filePath="C:\\Users\\zwk\\PycharmProjects\\DataStructureAndAgrithom\\fourletterwords.txt"
wordGraph=BuildGraph(filePath)

bfs(wordGraph,wordGraph.getVertex("FOOL"))

traverse(wordGraph.getVertex("SAGE"))

print(wordGraph.getVertex("SAGE").getDistance())

# import sys
# print(sys.maxsize+3)