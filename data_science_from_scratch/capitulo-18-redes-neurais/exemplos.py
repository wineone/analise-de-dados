from funcoes_capitulo_18 import *


network = [
    [ 
      [30,30,-40], # neuronio and
      [30,30,-20]  # neuronio or
    ],
    [ 
      [-70,70,-30] # neuronio de saida not and
    ] 
] # primeira rede neural codada meus amigos KKKK

for a in [0,1]:
    for b in [0,1]:
        print(a,b,feed_foward(network,[a,b])[-1] ) # probabilidade de saida para cada conjunto de valores


