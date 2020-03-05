import sys
sys.path.append("../capitulo-4-algebra-linear")
from funcoes_capitulo_4 import *
import random



def derivate(f,x,h = 0.0000000001):
    """
        definição da derivada, note que usamos o nome completo da derivada
        e usamos um h tendendo a zero como forma de imitar o limite
    """
    return (f(x + h) - f(x)) / h


def square(x):
    """
        retorna o valor ao quadrado
    """

    return x ** 2

def derivate_square(x):
    """
        retorna a derivada verdadeira da função square
    """
    return 2 * x


def partial_derivate(f,v,i,h = 0.0000000001):
    """
        calcula a derivada parcial do iésimo indice do meu vetor de funções
    """

    nv = [val + (h if ind == i else 0) for ind,val in enumerate(v)]

    return (f(nv) - f(v)) / h


def estimate_gradient(f,v,h = 0.0000000001):
    """
        retorna o vetor das derivadas parciais
    """

    return [partial_derivate(f,v,i,h) for i in range(len(v))]


def step(vetor, gradi, step = -0.01):
    """
        da um passo na descida do gradiente,
        o passo é dado com a soma do tamanho do passo vezes a derivada parcial no indice
    """
    return [v + g * step for v,g in zip(vetor,gradi)]


def square_list(lista):
    """
        retorna a seguinte função 
        f(l) = l[0]**2 + l[1]**2 ... etc
    """
    return sum([i ** 2 for i in lista])


def in_random_order(data):
    """
        embaralha os dados e os retorna como um iterador
    """
    indis = list(range(len(data)))
    random.shuffle(indis)

    for i in indis:
        yield data[i]


def minimize_stochastic(target, gradient, x, y, theta, alpha = 0.01):
    """
        função para fazer a descida stocastica do gradiente.
        a descida stocastica é caracterizada pela propriedade adtiva da função de erro 
        do nosso modelo. se ela for aditiva podemos computar o erro para cada ponto e atualizar os valores.
        note que estamos minimizando o valor
    """

    data  = list(zip(x,y))

    min_theta, min_value = theta, float('inf')

    iterations_not_impro = 0
    alpha_0 = alpha


    while iterations_not_impro < 100: # enquanto não convergir faça

        value = sum([target(val,tar,theta) for val,tar in data]) # erro global


        if value < min_value:
            min_theta, min_value = theta, value
            iterations_not_impro = 0
            alpha_0 = alpha
        else:
            iterations_not_impro += 1
            alpha_0 *= 0.9 # diminuimos o tamanho do passo
        
        # agora faremos a descida estocastica

        for val,tar in in_random_order(data):
            grad = gradient(val,tar,theta)
            theta = vector_subtract(theta,scalar_multiply(alpha_0,grad)) # da um passo

    return min_theta

def negate(f):
    """
        retorna -f para cada entrada da função
    """

    return lambda *args: -f(*args)

def negate_all(grad):
    """
        retorna o negado da derivada, note que precisamos disso
        quando se trata de uma derivada já derivada
    """

    return lambda *args: [-y for y in grad(*args)]

def maximize_stochastic(target, gradiente, x, y, theta, alpha=0.01):
    """
        função para fazer a descida stocastica do gradiente.
        a descida stocastica é caracterizada pela propriedade adtiva da função de erro 
        do nosso modelo. se ela for aditiva podemos computar o erro para cada ponto e atualizar os valores.
        note que estamos maximizando o valor
    """
    return minimize_stochastic(negate(target),negate_all(gradiente),x,y,theta,alpha)


def funcao_linear(a,x):
    return a*x

def erro_quad(x,y,tar):
    return (y - funcao_linear(tar[0],x))**2

def derivate_erro_quad(x,y,tar,h=0.00000001):
    return [(erro_quad(x,y,[i +h for i in tar]) - erro_quad(x,y,tar)) / h]


def minimize_batch(target, gradient, come, tolerance = 0.00000000001):
    """
        usa o gradient descendent para minimizar uma função, note que eh uma versão mais lenta que a estocastica
    """

    step_sizes = [100,10,1,0.1,0.01,0.001,0.0001,0.00001]

    theta = come
    value = target(theta)

    while True:

        derivada = gradient(theta)

        next_theta = [step(theta,derivada, -size) for size in step_sizes]

        next_theta = min(next_theta, key = target)

        next_value = target(next_theta)

        if abs(next_value - value) < tolerance:
            return next_theta
        else:
            theta,value = next_theta,next_value



def maximize_batch(target, gradient, come, tolerance = 0.00000000001):
    """
        retorna a versão que maxiza o gradiente descendent na versãoo
    """

    return minimize_batch(negate(target),negate_all(gradient),come,tolerance)