#%%
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#%%
def data(size):
    x = []
    y = []
    
    for count in range(size):
        x.append(random.randint(1,199))
        y.append(random.randint(1,199))
    return x,y

#%%
def dist(x,y):
    res = math.sqrt(x.__pow__(2)+y.__pow__(2))
    return round(res)

#%%
def connect(x,y):
    #For every point in the graph...
    for nodes in range(len(x)):
        best = [[400,0],[400,0],[400,0]]
        highest = 400
        
        #Go over every OTHER point and do...
        for node in range(len(x)):
            #If the distance in pythagoras' theorm is less than the highest 
            if (dist(x[node]-x[nodes],y[node]-y[nodes]) < highest):
                best[0] = [dist(x[node]-x[nodes],y[node]-y[nodes]), node]
                best.sort(reverse=True)
                highest = best[0][0]
        for marks in range(len(best)):
            plt.plot([x[nodes], x[best[marks][1]]], [y[nodes], y[best[marks][1]]])

#%%

size = 100
x, y = data(size)

plt.scatter(x, y, color='r')
connect(x,y)
#for v in range(19):
#    plt.plot([x[v],x[v+1]], [y[v],y[v+1]])
plt.show()