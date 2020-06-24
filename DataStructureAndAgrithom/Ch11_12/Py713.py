from basis.priorityQueue import PriorityQueue
from Ch11_12.Py703 import  Graph
import sys
# 最小生成树，是一个贪心算法
def prim(G,start):
    pq=PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        # 出队的节点是上一次循环得到的最小权重
        currentVert=pq.delMin()
        for nextVert in currentVert.getConnections():
            newCost=currentVert.getWeight(nextVert)
            # nextVert in pq，可以安全添加的边（一端顶点在树中，另一端不在树中）
            if nextVert in pq and newCost <nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert,newCost)

if __name__=="__main__":
    G = Graph()
    ndedge = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1),
              ('B', 'D', 1), ('B', 'E', 4), ('C', 'F', 5),
              ('D', 'E', 1), ('E', 'F', 1), ('F', 'G', 1)]
    for nd in ndedge:
        G.addEdge(nd[0], nd[1], nd[2])
        G.addEdge(nd[1], nd[0], nd[2])
    start = G.getVertex('A')
    prim(G, start)
    for g in G:
        print(g,g.getDistance(),g.getPred())