import timeit
import random
import matplotlib.pyplot as plt
x1=[]
y1=[]
y2=[]
for i in range(10000,210001,20000):
    t= timeit.Timer("random.randrange(%d) in x"%i,"from __main__ import random,x")
    x=list(range(i))
    lst_time=t.timeit(number=1000)

    x={j:None for j in range(i)}
    d_time=t.timeit(1000)
    x1.append(i)
    y1.append(lst_time)
    y2.append(d_time)
    print("%d,%.3f,%.3f"%(i,lst_time,d_time))

plt.scatter(x1,y1,marker="o",label="lst_time")
plt.scatter(x1,y2,marker="x",label="d_time")
plt.grid(True)
plt.xlabel("iteration")
plt.ylabel("iteration_time")
plt.legend(loc="upper left")
plt.title("list_compare_dict")
plt.show()