from funcoes_capitulo_14 import *
import random


# teste da regressão linear

data = [
    [0.8,3.5],
    [1.5,4.9],
    [1,5.1],
    [2,4.9],
    [2,6],
    [2.4,6.8],
    [2.9,6.7],
    [3,7],
    [3.1,7.3],
    [3.3,7.4],
    [3,7.2],
    [3.7,7.6],
    [3.9,8],
    [3.7,8.2],
    [4.2,8.4]
]


alpha,beta = minimized_error(*zip(*data))

print(alpha,beta)

print("nosso modelo explica,",r_squared(*zip(*data),alpha,beta))

## usando descida do gradiente estocastica

theta = [random.random(),random.random()]

alpha,beta = minimize_stochastic(squared_error,derivate_squared_error,*zip(*data),theta,-0.0001)

print(alpha,beta)