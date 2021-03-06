from basis.priorityQueue import PriorityQueue
from Ch11_12.Py703 import  Graph
# 只能处理大于0的权重 ，如果出现负数权重会陷入无限循环
def dijkstra(aGraph,start):
    # 解决带权边最短路径
    # 顶点的访问次序由一个优先队列来控制，开始顶点距离设为0
    # 算法复杂度O（v+e)*logV
    pq=PriorityQueue()
    start.setDistance(0)
    # 对所有顶点建堆，形成优先队列
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        # 优先队列出队的总是距离最小的顶点
        currentVert=pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist=currentVert.getDistance()+currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                # 修改出队顶点所连接顶点的dist，并逐个重排队列
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)


if __name__=="__main__":
    G = Graph()
    ndedge = [('u', 'v', 2), ('u', 'w', 5), ('u', 'x', 1),
              ('v', 'x', 2), ('v', 'w', 3), ('x', 'w', 3),
              ('x', 'y', 1), ('w', 'y', 1), ('w', 'z', 5),
              ('y', 'z', 1)]
    for nd in ndedge:
        G.addEdge(nd[0],nd[1],nd[2])
        G.addEdge(nd[1],nd[0],nd[2])
    start=G.getVertex("u")
    dijkstra(G,start)

    for v in G:
        print(v,v.getDistance(),v.getPred())