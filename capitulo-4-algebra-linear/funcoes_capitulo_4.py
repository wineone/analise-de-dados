from __future__ import division
import math

def vector_add(a,b):
    """
        retorna a soma de dois vetores
    """
    return [i+j for i,j in zip(a,b)]


def vector_sum(vectors):
    """
        faz a soma de n vetores dois a dois
    """

    prim = vectors[0]
    for i in vectors[1:]:
        prim = vector_add(prim,i)

    return prim

def vector_subtract(a,b):
    """
        faz a subtração de a - b
    """

    return [i-j for i,j in zip(a,b)]


def scalar_multiply(c,v):
    """
        faz a multiplicação de um escalar por um vetor, note que c é um numero
        e v um vetor, multiplicação por escalar aumenta o tamanho do vetor
    """

    return [c * i for i in v]


def vector_mean(*vectors):

    """
        calcula a média das somas de todos os vetores
    """

    n = len(vectors)

    return scalar_multiply(1/n,vector_sum(*vectors))

def dot(a,b):
    """
        calcula o produto escalar de dois vetores, mas o que é o produto escalar:

        é o modulo de b vezes o tamanho da projeção de a em b:

        sum(a*b) = ||a||* cos 0 * ||b||
    """

    return sum([i*j for i,j in zip(a,b)])



def sum_of_squares(a):
    """
        soma dos quadrados
    """
    return dot(a,a)

def magnitude(a):

    """
        retorna o tamanho de um vetor
    """

    return math.sqrt(sum_of_squares(a))

def distance(a,b):
    """
        calcula a distancia de um vetor a para um vetor b
    """

    return magnitude(vector_subtract(a,b))


def shape(A):
    """
        retorna o shape de uma matriz
    """

    return len(A),len(A[0])



def get_row(A,i):
    """
        retorna uma linha da matriz
    """

    return A[i]

def get_column(A,i):
    """
        retorna uma coluna da matriz
    """

    return [A[k][i]  for k in range(len(A))]


def make_matrix(n,k,f):
    """
        constroi uma matriz de acordo com os argumentos e a função passada
    """
    return [[f(j,i) for i in range(k)] for j in range(n)]

    
def is_diagonal(i,j):
    """
        função para construir uma matriz diagonal
    """
    return 1 if i == j else 0