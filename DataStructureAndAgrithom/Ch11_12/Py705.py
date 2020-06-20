from Ch11_12.Py704 import BuildGraph
from basis.Queue import Queue

def bfs(g,start):
    start.setDistance(0)
    start.setPred=None
    vertQueue=Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        currentVert=vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor()=="white"):
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor("black")

def traverse(y):
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