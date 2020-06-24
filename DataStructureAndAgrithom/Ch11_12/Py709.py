from Ch11_12.Py703 import  Graph
# 实现通用的深度优先搜索，算法复杂度为O（v+E）
# 顶点增加发现时间（设置灰色）和结束时间（设置黑色）属性
class DFSGraph(Graph):
    def __iter__(self):
        super.__init__()
        self.time=0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor("white")
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor()=="white":
                # 每调用一次dfsvisit生成一棵树
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        # 当前顶点设置为灰色，表示正在探索
        startVertex.setColor("gray")
        self.time+=1
        # 设置发现时间
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor()=="white":
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        # 探索完所有startVertex的邻接顶点后，设置为黑色，设置结束时间
        startVertex.setColor("black")
        self.time+=1
        startVertex.setFinish(self.time)

# 图的应用：拓扑排序 --> 以动作为顶点，以先后次序为有向边  --> 处理一个DAG \
# --> 按照每个顶点的结束时间，从大到小排序，输出这个次序下的顶点列表

# 强连通分支