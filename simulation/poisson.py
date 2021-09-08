import random
import math
import numpy as np 
import matplotlib.pyplot as plt


def n(la,limit):
    N_l = []
    for i in range(limit):
        v = 1
        k=-1
        while not (v < math.exp(-la)):
            v = random.uniform(0,1)
            k += 1 
        N_l.append(k)
    return N_l
def chi(x,lst):
    return int(x in lst)
def poissonProcess(alpha,L):
    N =  np.random.poisson(alpha*L)
    X = np.random.exponential(alpha,N)
    Y = np.random.uniform(0,L,N) 
    return X,Y

xx,yy = poissonProcess(0.8,150)
plt.scatter(xx,yy)
plt.show()
