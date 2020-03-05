from funcoes_capitulo_10 import *


data = [
    [1,-1,3,-3],
    [2,-2,4,-4],
    [3,-5,5,-5],
    [4,-6,7,-8],
    [5,-7,8,-9]
]

ma = correlation_matriz(data)

for i in ma:
    print(i)

plot_matriz_dispersao(data)