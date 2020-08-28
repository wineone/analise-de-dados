import math
import sys
sys.path.append("../capitulo-4-algebra-linear")
from funcoes_capitulo_4 import *



def logistic(x):
    """
        retorna o valor da função logistica, note que ela tem assintotas em 0 e 1
    """
    return 1 / (1 + math.exp(-x))

def logistic_log_likelihood_i(x_i, y_i, beta):
    """
        retorna as probabilidades de uma determinado exemplo pertencer aquela classificação
    """

    if y_i == 1:
        return math.log(logistic(dot(x_i,beta)))
    else:
        return math.log(1 - logistic(dot(x_i,beta)))



def logistic_log_gradient_i(x_i,y_i,beta):
    """
        retorna a derivada parcial para cada beta na função 
    """

    return [(y_i - logistic(dot(x_i,beta))) * x for x,_ in zip(x_i,beta)] # nao faço ideia de por que essa função é assim


def predict(modelo, x_i):
    """
        faz uma previsão com probabilidade entre 0 e 1 de o usuario ser true
    """

    return logistic(dot(modelo,x_i))