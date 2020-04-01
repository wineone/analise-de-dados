
import random
import math


def random_kid():
    """
        função que gera um filho de uma familia
    """
    return random.choice(["boy","girl"])


def normal_pdf(x,u=0,des=1):
    
    """
        (probability density function)
        função densidade de probabilidade da normal, integramos essa formula e ganhamos a probabilidade em um intervalo
    """

    return math.exp(-(x-u)**2 / 2 / des**2) / (math.sqrt(2*math.pi) * des)


def normal_cdf(x,u=0,des=1):
    """
        (cumulative density function)
        função de densidade acumulada, fala a probabilidade que vem antes de um ponto P(x < Z)
    """
    return (1+math.erf((x-u) / math.sqrt(2)/ des)) / 2


def inverse_normal_cdf(x,u=0,des=1,tole = 0.00000000001):

    """
        função que inverte a função de soma acumulada da normal,
        -> dada uma probabilidade ela retorna o X tal que P(x < X)
    """

    if u != 0 or des != 1:
        return u + des * inverse_normal_cdf(x)

    l = -10
    r = 10

    mid = (l + r) / 2

    res = normal_cdf(mid)

    while abs(res - x) > tole:

        mid = (r + l)/2
        res = normal_cdf(mid)

        if res > x:
            r = mid
        elif res < x:
            l = mid        
        else:
            break
        
    
    return mid

def bernoulli(p):
    """
        variavel que é 0 ou 1
    """
    return 1 if random.random() < p else 0

def media_bernoulli(n,p):
    """
        faz a média de n lançamentos de bernoulli
    """
    return int((sum([bernoulli(p) for _ in range(n)]) / n) * 1000) / 1000


def binominal(n,p):
    """
        faz um ensaio de binomial com parametro n e p
    """
    return sum([bernoulli(p) for _ in range(n)])