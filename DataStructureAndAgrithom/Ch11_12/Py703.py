import sys
class Vertex:
    # 顶点是图的基本组成部分，具有名称标识key，也可以携带数据项payload
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        self.color="white"
        self.dist=sys.maxsize
        self.pred=None
        self.disc=0
        self.fin=0

    def addNeighbor(self,nbr,weight=0):
        # key（顶点），value（权重）
        self.connectedTo[nbr]=weight

    def setDistance(self,d):
        self.dist=d

    def setColor(self,color):
        self.color=color

    def setPred(self,p):
        self.pred=p

    def setDiscover(self,dtime):
        self.disc=dtime

    def setFinish(self,ftime):
        self.fin=ftime

    def getFinish(self):
        return self.fin

    def getDiscover(self):
        return  self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color


    def __str__(self):
        # return str(self.id)+" conected to : "+str([x.id for x in self.connectedTo])
        return str(self.id)#+" connected to : "+str([x.id for x in self.connectedTo])
        # return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"

    def getConnections(self):
        # connectedTo为一个字典，返回字典的key（顶点），value（权重）
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    # 图由顶点和边组成
    # DAG：有向无圈图
    # GRAPH实现有两种：邻接矩阵-》稀疏矩阵、邻接列表-》（一个包含所有顶点的列表，每个顶点在关联一个与自身有链接关系的列表
    def __init__(self):
        # 顶点列表
        self.vertList={}
        # 顶点个数
        self.numVertices=0

    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        newVertex=Vertex(key)
        # key为字典的索引，value为顶点
        self.vertList[key]=newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        # 添加的是一个有向边
        if f not in self.vertList:
            # 不存在的顶点先添加
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        # 调用起始顶点的addNeighbor方法添加邻接边
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        # 迭代方法，可以用for v in G 获得每一个顶点
        return iter(self.vertList.values())

if __name__=="__main__":
    g=Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    # g.addEdge(0, 1, 5)

    for i in g:
        print(i)

    print(g.vertList)

    for v in g:
        for w in v.getConnections():
            print("(%s,%s)"%(v.getId(),w.getId()))