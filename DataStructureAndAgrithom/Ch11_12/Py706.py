from Ch11_12.Py703 import  Graph


def genLegalMoves(x,y,bdSize):
    newMoves=[]
    moveOffsets=[(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]

    for i in moveOffsets:
        newX=x+i[0]
        newY=y+i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x>=0 and x<bdSize:
        return True
    else:
        return False

def knightGraph(bdSize):
    ktGraph=Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId=posToNodeId(row,col,bdSize)
            newPositions=genLegalMoves(row,col,bdSize)
            for e in newPositions:
                nid=posToNodeId(e[0],e[1],bdSize)
                ktGraph.addEdge(nodeId,nid,bdSize)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return row*bdSize+col

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


def knightTour(n,path,u,limit):
    u.setColor("gray")
    path.append(u)
    if n<limit:
        # nbrList=list(u.getConnections())
        nbrList=orderByAvail(u)
        i=0
        done=False
        while i<len(nbrList) and not done:
            if nbrList[i].getColor()=="white":
                done=knightTour(n+1,path,nbrList[i],limit)
            i=i+1
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






















