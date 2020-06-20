# -*- encoding=utf-8 -*-
from basis.Queue import Queue
import random
class Printer:
    def __init__(self,ppm):
        # ppm page per minute
        self.pagerate=ppm
        self.currentTask=None
        # 当前打印任务剩余执行时间
        self.timeRemaining=0

    def tick(self):
        # 时间流逝，每秒剩余时间减一
        if self.currentTask != None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None
    # check打印机是否busy
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    # 开启一个新的打印任务
    def startNext(self,newTask ):
        self.currentTask=newTask
        # 将ppm每分钟转化为s
        self.timeRemaining=newTask.getPages()\
            *60/self.pagerate

class Task:
    def __init__(self,time):
        # 任务生成的时间戳
        self.timestamp=time
        # 随机生成每个任务的页数
        self.pages=random.randrange(1,21)
    #     获取时间戳
    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages
    # 计算当前任务从生成到执行等待的时间
    def waitTime(self,currentTime):
        return currentTime-self.timestamp
# 每三分钟生成一个打印任务
def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False
# numSeconds 给定一个时间区间
def simulation(numSeconds,pagesPerMin):
    labPrinter=Printer(pagesPerMin)
    printQueue=Queue()
    waittingTimes=[]
    # 在0-3600s这个时间段内，时间不断流逝
    for currentSecond in range(numSeconds):
        if newPrintTask():
            # 生成一个任务，并且将生成时间戳赋给它
            task=Task(currentSecond)
            # 加入队列
            printQueue.enqueue(task)
        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask=printQueue.dequeue()
            waittingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)
        labPrinter.tick()
    averageWait=sum(waittingTimes)/len(waittingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining"\
          %(averageWait,printQueue.size()))

if __name__=="__main__":

    for i in range(10):
        simulation(3600,10)