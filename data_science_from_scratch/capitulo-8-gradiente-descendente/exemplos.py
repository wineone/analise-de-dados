from funcoes_capitulo_8 import *
import random
import sys
sys.path.append("../capitulo-4-algebra-linear")
from funcoes_capitulo_4 import *

## primeira implementação da descida do gradiente

tam_vetor = 5

v = [random.randint(-10,10) for i in range(tam_vetor)]

tolerance = 0.00000001

print("vetor antes da descida,",v)

while True:
    gradiente = estimate_gradient(square_list,v)
    novo_v = step(v,gradiente,step=-0.01)
    if distance(gradiente,novo_v) < tolerance:
        break
    v = novo_v

print("vetor depois da descida,",v) # muito legal


# descida estocastica do gradient

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
y = [2,4,5,9,9,13,13,17,18,22,22,23,26,28]

print("descida estocastica, o resultado deve ser em torno de 2,",minimize_stochastic(erro_quad,derivate_erro_quad,x,y,[-5]))