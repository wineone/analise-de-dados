from collections import Counter
import sys
sys.path.append("../capitulo-4-algebra-linear/")
from funcoes_capitulo_4 import *
import math


# tendencias centrais

def mean(x):
    """
        retorna a média de um conjunto de dados
    """

    return sum(x) / len(x)



def median(x):
    """
        retorna a mediana do cojunto de dados,
        o valor que deixa 50% dos valores para trás
    """

    n = len(x)

    ordenado = sorted(x)

    metade = n//2

    if(n%2):
        return ordenado[metade]
    else:
        return (ordenado[metade] + ordenado[metade-1]) / 2

    

def quantile(x,p):
    """
        retorna o valor que deixa aquela porcentagem dos dados para trás
    """

    n = len(x)

    valor = int(n * p)

    return sorted(x)[valor]


def mode(x):
    """
        retorna os elementos mais frequentes da colecao de dados
    """
    contador = Counter(x)

    maximo = max(contador.values())

    return [i for i,j in contador.items() if j == maximo]


# dispersão

def amplitude(x):
    """
        amplitude é a diferença do maior e do menor valor,
        não é indicado pois

        0 0 0 0 0 100
        0 50 50 50 100

        tem a mesma amplitude
    """
    return max(x) - min(x)

def diff_media(x):
    """
        retorna a diferença da média com todos os valores no conjunto de dados
    """

    media = mean(x)

    return [media - i for i in x]

def variance(x):
    """
        retorna a variancia dos dados, ela é calculada como o quadrado da
        diferença dividido pela quantidade dados
    """

    desviacoes = diff_media(x)
    quadrados = sum_of_squares(desviacoes)

    return quadrados / len(x)


def standard_deviation(x):
    """
        desvio padrão é definido como a raiz da variancia
    """
    return math.sqrt(variance(x))


def interquartile_range(x):
    """
        distancia interquartilica é a diferença os quantis 0.75 - 0.25
    """
    return quantile(x,0.75) - quantile(x,0.25)



def covariance(x,y):
    """
        a covariancia mede o quanto duas variaveis variam no conjunto de suas médias,

        -> produto do array de diferenças da média
    """

    n = len(x)

    return dot(diff_media(x),diff_media(y)) / n

def correlation(x,y):
    """
        varia entre -1 e 1 e indica a correlação entre as variaveis,
        a covariancia divida pelos desvios padrão
    """

    std_devx = standard_deviation(x)
    std_devy = standard_deviation(y)

    if(std_devx == 0 or std_devy == 0):
        return 0
    
    return covariance(x,y) / std_devx / std_devy


