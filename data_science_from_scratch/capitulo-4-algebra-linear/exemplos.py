
from funcoes_capitulo_4 import *

a = [1,2,3]

b = [1,2,3]

c = [5,5,5]

print("a soma de dois vetores",vector_add(a,b))

print("outra função de soma,",vector_sum(a,b))

print("a menos b",vector_subtract(a,b))

print("a vezes 3",scalar_multiply(3,a))

print("média dos vetores,",vector_mean(a,c))

print("produto escalar de a e c,",dot(a,c))

print("o tamanho de c",magnitude(c))


print("a distancia de a e c",distance(a,c))


# matrizes

A = [
    [1,2,3],
    [4,5,6]
    ]

print("shape de A,",shape(A))

print("linha 1,",get_row(A,0))

print("columa 1,",get_column(A,1))

print("matriz diagonal,",make_matrix(3,3,is_diagonal))