import sys
import random
sys.path.append("../capitulo-4-algebra-linear")
sys.path.append("../capitulo-8-gradiente-descendente")
sys.path.append("../capitulo-5-estatistica")
sys.path.append("../capitulo-6-probabilidade")
from funcoes_capitulo_4 import *
from funcoes_capitulo_5 import *
from funcoes_capitulo_8 import *
from funcoes_capitulo_6 import *



def predict(x_i, beta):
    """
        para predizer o resultado de um modelo, nós usaremos o produto escalar

        e para manter a multiplicação correta usaremos

        x_1 = [1, x1, x2,..,xk]

        beta = [alpha, b1, b2, ..., bk]
    """

    return dot(x_i,beta)

def erro_mult(x, y, beta):
    """
        retorna o erro do valor predito pelo valor real
    """

    return y - predict(x,beta)

def squared_erro_mult(x,y,beta):
    """
        retorna o erro ao quadrado do valor predito pelo valor real
    """

    return erro_mult(x,y,beta) ** 2

def squared_erro_mult_gradient(x, y, beta):
    """
        retorna a derivada parcial para todas as dimensoes de x
    """

    return [ -2 * x_i * erro_mult(x ,y ,beta) for x_i in x]

def estimate_beta(x,y):
    """
        faz a regressão multipla para os valores de x e y, mas note que os valores de x
        devem começar com uma coluna de 1's para facilitar os calculos
    """
    theta = [random.random() for _ in x[0]]
    return minimize_stochastic(squared_erro_mult,squared_erro_mult_gradient,x,y,theta,0.001)


def bootstrap_sample(data):
    """
        retorna uma lista como tamanho do dataset mas com amostras aleatorias com reposição
    """

    return [random.choice(data) for _ in data]

def bootstrap_statistic(data, func, num):
    """
        aplica a função a cada bootstrap_sample e faz isso num vezes
    """

    return [func(bootstrap_sample(data)) for _ in range(num)]

def estimate_sample_junto(sample):
    """
        função que descompacta uma tupla (x,y)
    """
    x,y = zip(*sample)

    return estimate_beta(x,y)


def p_value(media, desvio):
    """
        calcula a probabilidade de encontrar um valor tão grande quanto aquele naquele conjunto de dados,
        note que a media é Bj que é a estimativa para o beta no conjunto de dados
        e o desvio é o desvio padrão de varios betas calculados com datasets que foram gerados sinteticamente
        escolhendo aleatoriamente com reposição, note que quanto maior a variancia maior vai ser a largura da curva 
        normal pois h0 = Bj = 0
        então a padronização é da forma z = Bj - 0 / desvio dos datasets gerados
    """

    if media > 0:
        return 2 * (1 - normal_cdf(media / desvio))
    else:
        return 2 * normal_cdf(media/desvio)


