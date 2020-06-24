from Ch11_12.Py703 import  Graph

# 骑士周游问题求解

def genLegalMoves(x,y,bdSize):
    # 当前坐标下一步的合法走棋位置，最多8个
    newMoves=[]
    moveOffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]

    for i in moveOffsets:
        newX=x+i[0]
        newY=y+i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    #     返回当前节点的下一步和发走棋位置构成的列表
    return newMoves

def legalCoord(x,bdSize):
    # 确认新生成的坐标，没有超出棋盘
    if x>=0 and x<bdSize:
        return True
    else:
        return False

def knightGraph(bdSize):
    ktGraph=Graph()
    # 遍历所有格子，根据合法走棋位置建图
    # 8*8的棋盘有336条边，相比全连接4096，仅8.2%,是一个稀疏图
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId=posToNodeId(row,col,bdSize)
            newPositions=genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid=posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid,bdSize)
    return ktGraph

def posToNodeId(row,col,bdSize):
    # 根据当前坐标转换为节点号
    return row*bdSize+col


# 算法改进，修改了遍历下一格的次序，将u的合法目标棋盘格排序为：具有最少合法移动目标的格子优先搜索
def orderByAvail(n):
    resList=[]
    for v in n.getConnections():
        if v.getColor()=="white":
            c=0
            for w in v.getConnections():
                if w.getColor()=="white":
                    c=c+1
            resList.append((c,v))
    # reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
    resList.sort(key=lambda x:x[0])
    return [y[1] for y in resList]

# 采用深度优先搜索算法解决骑士周游问题，深度优先搜索算法沿着树的单支尽量深入向下搜索
# 如果到无法继续的程度还没有找到问题的解（所有合法格子都已经被搜索过），返回上一层再搜索下一支
# 引入栈记录路径，实施返回上一层的操作，因为要回溯离他最近的节点，所以采用栈
# 未改进的算法（nbrList=list(u.getConnections())）复杂度为k的n次方，n为棋盘的格数
def knightTour(n,path,u,limit):
    # n：层次，path：路径，u：当前节点，limit：搜索总深度
    u.setColor("gray")
    # 当前顶点加入路径
    path.append(u)
    if n<limit:
        # 对所有合法路径逐一深入
        # nbrList=list(u.getConnections())
        nbrList=orderByAvail(u)
        i=0
        done=False
        while i<len(nbrList) and not done:
            # 选择白色未探索过的顶点深入
            if nbrList[i].getColor()=="white":
                done=knightTour(n+1,path,nbrList[i],limit)
            i=i+1
        #如果当前节点邻接顶点都探索过，done任然为false，准备回溯，试本层下一个顶点，同时当前节点出栈，标记为白色
        if not done:
            path.pop()
            u.setColor("white")
    else:
        done=True
    return done


if __name__=="__main__":
    path=[]
    ktGraph=knightGraph(8)

    done=knightTour(0,path,ktGraph.getVertex(12),63)
    final=[]
    for i in path:
        final.append(i.getId())
    print(final)
    print(done)






















