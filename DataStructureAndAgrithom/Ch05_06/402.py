import turtle

# 简单入门
# t=turtle.Turtle()
# t.forward(500)
# turtle.done()

# 画一个正方形
# t=turtle.Turtle()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# turtle.done()

# 画一个五角星
# t=turtle.Turtle()
# t.pencolor("green")
# t.pensize(3)
# for i in range(5):
#     t.forward(100)
#     t.right(144)
# t.hideturtle()
# turtle.done()

# 绘制螺旋
# t=turtle.Turtle()
# def drawSpiral(t,length):
#     if length>0:
#         t.forward(length)
#         t.right(90)
#         drawSpiral(t,length-5)
# drawSpiral(t,100)
# t.hideturtle()
# turtle.done()

# 绘制分形树
def tree(branch_len):
    if branch_len>5:            #树干太短不画，即递归结束条件
        t.forward(branch_len)   #画树干
        t.right(20)             #右倾斜20度
        tree(branch_len-15)     #递归调用，画右边的小树，树干减15
        t.left(40)              #想左转40度，即做倾斜20度
        tree(branch_len-15)     #    #递归调用，画右边的小树，树干减15
        t.right(20)             #向右回20度，即回正
        t.backward(branch_len)  #海归退回原位置
# 考虑branch_len=20就可以想明白
t=turtle.Turtle()
t.left(90)                      #默认向右，左转90度
t.penup()                       #抬笔
t.backward(100)
t.pendown()
t.pencolor("red")
t.pensize(3)
tree(100)
t.hideturtle()
turtle.done()


















