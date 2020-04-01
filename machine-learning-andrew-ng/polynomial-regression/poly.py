import numpy as np
import math
import matplotlib.pyplot as plt
import random

def plota(O, X,Y):
    r = np.dot(X,O)
    r = r.T[0]
    x = [a[1] for a in X]
    y = [a[0] for a in Y]
    
    plt.scatter(x,y)
    plt.plot(x,r,"r")
    plt.show()

def plota_pontos(X,Y):
    plt.scatter([a[1] for a in X],[a[0] for a in Y],s=0.3,alpha=0.5)
    plt.show()

def erro(O, X, Y):
    return (sum(np.dot(X,O) - Y)) ** 2

def gradient(O, X, Y, alpha = 0.1):
    ant = 0
    while abs(ant - erro(O,X,Y)[0]) > 0.001:
        ant = erro(O,X,Y)[0]
        print(ant)
        # atualização dos pesos
        aux = np.zeros((2,1))
        for line,r in zip(X,Y):
            a = np.array([[line[0]],[line[1]]])
            #print((np.dot(line,O) - r))
            aux +=  (np.dot(line,O) - r)[0] * a
        aux = 1/len(X) * aux
        O = O - (alpha*aux)

    return O

X = []
Xsqrt = []

for i in range(1000):
    X.append([1,i / 1000])
    Xsqrt.append([1,math.sqrt(i) / math.sqrt(1000)])

X = np.array(X)
Xsqrt = np.array(Xsqrt)

Y = []

for a,b in X:
    Y.append([math.sqrt(b)+random.randint(1,10)])

O = np.array(
    [
        [10],
        [0.8]
    ]
)

# s = gradient(O,X,Y)

# plota(s,X,Y)

s = gradient(O,Xsqrt,Y)

plota(O,Xsqrt,Y)

