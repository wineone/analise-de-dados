import sys
sys.path.append("../capitulo-5-estatistica")
sys.path.append("../capitulo-8-gradiente-descendente")
from funcoes_capitulo_5 import *
from funcoes_capitulo_8 import *



def predict(x, alpha, beta):
    """
        faz uma previsão da forma

        f(y) = alpha + beta*x
    """

    return alpha + beta*x


def error(x,y,alpha,beta):
    """
        retorna o erro de uma amostra para o seu valor predito
    """

    return y - predict(x,alpha,beta)

def sum_of_squared_error(xs ,ys, alpha, beta):
    """
        retorna a soma dos erros quadrados
    """

    return sum(error(x,y,alpha,beta)**2 for x,y in zip(xs,ys))

def minimized_error(x,y):
    """
        retorna os alhpa e beta com o erro minizado, usando aquelas formulas que foram
        aprendidas em estatistica (lembro sim, pod confiar)

        mas intuição:

        alpha = media de y - previsão de y com base em x

        logo alpha é o erro que sobrou da forma que o coeficiente angular é calculado

        beta = o quanto y varia * correlação de x,y / o quanto x varia

        isso  quer dizer que, o quanto y varia é explicado pela correlação
        dividido pelo quanto x varia
    """

    beta = correlation(x,y) * standard_deviation(y) / standard_deviation(x)

    alpha = mean(y) - beta * mean(x)

    return alpha, beta

def total_sum_of_squares(y):
    """
        retorna a diferença das médias ao quadrado de um cojunto de dados
    """
    return sum([v**2 for v in diff_media(y)])

def r_squared(x,y,alpha,beta):
    """
        calcula o quanto nosso modelo explica os dados:

        ele é calculado como 1 - erros ao quadrado / o quadrado das diferenças da média

        isso quer dizer que quando nosso erros ao quadrado forem baixos o modelo vai explicar bem
        os dados
    """

    return 1 - (sum_of_squared_error(x,y,alpha,beta) / total_sum_of_squares(y))

def squared_error(x,y,theta):
    """
        retorna o erro ao quadrado do esperado para o que foi resultante do modelo
    """
    alpha, beta = theta
    return error(x,y,alpha,beta)**2

def derivate_squared_error(x,y,theta):
    """
        retorna a derivada da função de erro para ser usada na descida do gradiente

        lembrete da derivada: lembrar de derivar a parte de dentro também
    """

    alpha, beta = theta

    return [2 * error(x,y,alpha,beta), 2 * error(x,y,alpha,beta) * x]


