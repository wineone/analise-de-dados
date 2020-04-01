import sys
sys.path.append("../capitulo-6-probabilidade")
from funcoes_capitulo_6 import *
import math


def normal_aproximation_to_binomial(n,p):
    """
        retorna a média e o desvio padrão de uma binomial definida com n bernoulli e probabilidade p
    """

    media = n*p
    des = math.sqrt(n*p*(1-p))
    
    return media,des


def normal_probability_below(x,media = 0, desvio = 1):
    """
        retorna a probabilidade abaixo de um determinado valor
    """
    return normal_cdf(x,media,desvio)

def normal_probability_above(x,media = 0, desvio = 1):
    """
        retorna a probabilidade de ser maior que um ponto
    """
    return 1 - normal_probability_below(x,media,desvio)

def normal_probability_between(lo,hi,media = 0, desvio = 1):
    """
        retorna a probabilidade de estar entre dois pontos
    """
    return normal_probability_below(hi,media,desvio) - normal_probability_below(lo,media,desvio)

def normal_probability_outside(lo,hi,media = 0, desvio = 0):
    """
        retorna a probabiliade de estar fora de dois valores
    """
    return 1 - normal_probability_between(lo,hi,media,desvio)

def normal_valor_abaixo(p,media = 0, desvio = 1):
    """
        retorna o valor que deixa aquela probabilidade abaixo, valor em x
    """

    return inverse_normal_cdf(p,media,desvio)

def normal_valor_acima(p,media = 0, desvio = 1):
    """
        retorna a probabilidade que deixa aquilo na calda da direita, valor em x
    """
    return inverse_normal_cdf(1-p,media,desvio)

def normal_two_sided_bounds(p,media = 0, desvio = 1):
    """
        retorna os valores que deixam a probabilidade especificada no meio
    """

    tail = (1 - p) / 2

    lo = normal_valor_abaixo(tail,media,desvio)
    hi = normal_valor_acima(tail,media,desvio)

    return lo,hi


def two_sided_p_value(x,media = 0, desvio = 1):
    """
        retorna o p value para um valor tão grande quanto aquele, assumindo que nossos dados são normais.
        é convensão que se o p value for menor que 5% rejeitamos h0
    """

    if x > media:
        return 2 * normal_probability_above(x,media,desvio)
    else:
        return 2 * normal_probability_below(x,media,desvio)


def upper_p_value(x,media = 0, desvio = 1):
    """
        retorna o p valor para o lado de cima, para testes unilaterais
    """

    return normal_probability_above(x,media,desvio)

def lower_p_value(x,media = 0, desvio = 1):
    """
        retorna o p valor para o lado de baixo, para testes unilaterais
    """

    return normal_probability_below(x,media,desvio)

def intervalo_de_confianca(p,media = 0, desvio = 1):
    """
        retorna o intervalo de confiança em torno da média para um conjunto de testes
    """

    return normal_two_sided_bounds(0.95,media,desvio)


def estimated_values(n,N):
    """
        retorna a média e o desvio padrão para uma proporção de uma amostra, assumindo que é normal
    """

    proporcao = n / N
    desvio = math.sqrt((proporcao * (1 - proporcao)) / N)

    return proporcao,desvio


def normalizado_test_ab(na,Na,nb,Nb):
    """
        retorna um valor com a diferença das normais das proporções para fazer um teste com p value depois
    """

    p_a,des_a = estimated_values(na,Na)
    p_b,des_b = estimated_values(nb,Nb)

    return (p_a - p_b) / math.sqrt(des_a ** 2 + des_b ** 2)


def valor_p_teste_ab(na,Na,nb,Nb):
    """
        faz o teste com o p value para as proporcoes de dois experimentos onde a hipotese nula é que as duas
        proporcoes são iguais, contra h1 são diferentes, com 5% de significancia.
        Observe que ela é bastante dependente do tamanho das amostras.
        Para amostra maiores a diferença é muito mais significativa e o p value vai ser menor.
    """

    x = normalizado_test_ab(na,Na,nb,Nb)
    return two_sided_p_value(x)