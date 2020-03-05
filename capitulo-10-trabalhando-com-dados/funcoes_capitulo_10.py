import math
from collections import Counter
from matplotlib import pyplot as plt
import sys
sys.path.append("../capitulo-6-probabilidade")
sys.path.append("../capitulo-4-algebra-linear")
sys.path.append("../capitulo-5-estatistica")
sys.path.append("../capitulo-8-gradiente-descendente")
from funcoes_capitulo_6 import *
from funcoes_capitulo_4 import *
from funcoes_capitulo_5 import *
from funcoes_capitulo_8 import *
from matplotlib import pyplot as plt
from collections import defaultdict
from functools import partial

def bucketize(point, bucketsize):
    """
        discretiza um ponto
    """
    return bucketsize * math.floor(point / bucketsize)


def counter_bucket(points, bucketsize):
    """
        faz a contagem de pontos discretizados
    """
    return Counter([bucketize(point,bucketsize) for point in points])

def plot_histogram(points, bucketsize, title=""):
    """
        plota um histograma com os pontos discretizados e
        as contagens dos seus buckets
    """
    dic = counter_bucket(points,bucketsize)

    plt.bar(list(dic.keys()),list(dic.values()),width=bucketsize - 1)
    plt.title(title)
    plt.show()


def random_normal():
    """
        retorna um valor da normal, note que esse valor é
        ele mesmo distribuido normalmente
    """
    return inverse_normal_cdf(random.random())


def correlation_matriz(data):
    """
        retorna uma matriz de correlação com uma combinação
        de todos os dados com todos os dados,
        note que a entrada é feita pelas colunas, imagine que
        ele recebe um csv
    """

    _,column = shape(data)

    def corre(i,j):
        """
            função auxiliar, note que ela está aqui dentro
            para ter acesso aos dados para que eles nao precisem
            ser passados por parametro
        """
        return correlation(get_column(data,i),get_column(data,j))
    
    return make_matrix(column,column,corre)

def plot_matriz_dispersao(data):
    """
        plot varios graficos com os graficos
        de dispersão com os dados 2 a 2
        tambem está no formato de csv
    """

    line, columns = shape(data)


    _,ax = plt.subplots(columns,columns)

    for i in range(columns):
        for j in range(columns):
            if i != j:
                ax[i][j].scatter(get_column(data,i),get_column(data,j))

            if not i == columns -1:
                ax[i][j].xaxis.set_visible(False)
            if not j == 0:
                ax[i][j].yaxis.set_visible(False)
    plt.show()

def parse_row(row, parsers):
    """
        converte uma linha para o formato desejado
    """

    return [try_or_none(parse)(value) if parse is not None else value for parse,value in zip(parsers,row)]


def parse_data(data,parsers):
    """
        retorna um iterador para as linhas dos dados
    """

    for dado in data:
        yield parse_row(dado,parsers)


def try_or_none(fun):
    """
        tenta a funcao ou retorna none se nao puder
    """

    def nova(x):
        """
            faz uma função "safe"
        """
        try:
            return fun(x)
        except:
            return None
            
    return nova

## funções para agrupar dados

def try_parse_field(field,value,dict_parse):
    """
        tenta tratar o dado com a fução correspondente
    """
    parse = dict_parse.get(field)

    if parse is not None:
        return try_or_none(parse)(value)
    else:
        return value

def parse_dict(input_dict, parse_dict):
    """
        converte um dicionario de acordo com as funções dadas pelo
        dicionario de parametro
    """

    return {key: try_parse_field(key,value,parse_dict) for key,value in input_dict.items()}

def parse_data_dict(data, parse):
    """
        converte todos os dados
    """
    
    for i in data:
        yield parse_dict(i,parse)


def picker(field_name):
    """
        retorna uma função que recolhe um campo de um dicionario passado
    """

    return lambda row: row[field_name]

def pluck(field_name,rows):
    """
        retorna uma lista de valores retirados da lista de dicionario de 
        acordo com o campo passado por paramentro
    """
    return map(picker(field_name),rows)

def group_by(grouper,rows, value_transformation=None):
    """
        função que agrupa os dados de acordo com a função que foi passada
        no grouper.

        note que ele segue o padrão do sql.

        -> select por
        -> esses dados
        -> aplique essa função no resultado do agrupamento
    """

    agru = defaultdict(list)

    for row in rows:
        agru[grouper(row)].append(row)
    
    if value_transformation is None:
        return agru
    else:
        return {key: value_transformation(value) for key,value in agru.items()}

## redimensionando nossos dados


def scale(data_matriz):
    """
        retorna todas as médias e desvios padrão,
        note que estamos tratando de amostras
    """

    lines,columns = shape(data_matriz)

    medias = [mean(get_column(data_matriz,i)) for i in range(columns)]

    desvios = [standard_deviation(get_column(data_matriz,i)) for i in range(columns)]

    return medias,desvios



def rescale(data):
    """
        redimensiona os dados para que eles estejam no formato 
        desvios padrão a partir da média
    """

    medias, desvios = scale(data)

    def rescale_ij(i,j):
        if desvios[j] > 0:
            return (data[i][j] - medias[j]) / desvios[j]
        else:
            return data[i][j]

    lin,col = shape(data)
    return make_matrix(lin,col,rescale_ij)

def de_mean_matriz(X):
    """
        retorna uma nova matriz com os dados com média 0
    """

    l,c = shape(X)
    medias,_ = scale(X)

    return make_matrix(l,c,lambda i,j: X[i][j] - medias[j])

def direction(w):
    """
        dado um vetor de tamanho n, retorna um novo vetor de tamanho 1
    """
    tam = magnitude(w)
    return [i / tam for i in w]

def directional_variance(v,w):
    """
        retorna a projeção escalar do vetor v em w, note que w vai ser um vetor
        com tamanho 1 e nós queremos maximizar essa variancia pois quanto maior a variancia
        mais os dois vetores vão estar perto um do outro
    """

    return dot(v,direction(w)) ** 2

def direcional_variance_data(X,w):
    """
        função de soma de erro quadrático para a projeção
    """
    return sum(directional_variance(x,w) for x in X)

def direcional_variance_gradient(v,w):
    """
        retorna a derivada da função do produto escalar dos dois vetores,
        note que eu não sei o que é essa derivada, então fudeu neh
    """

    projection_lenght = dot(v,direction(w))

    return [2 * projection_lenght * v_i for v_i in v]

def direcional_variance_gradient_data(X,w):
    """
        a soma dos erros em todos os pontos do nosso cojunto de dados
    """

    return vector_sum([direcional_variance_gradient(x,w) for x in X])

def func(w,i,v):
    h = 0.000000001
    w1 = [x + h if ind == i else 0 for ind,x in enumerate(w)]
    return (directional_variance(v,w1) - directional_variance(v,w)) / h

def direcional_variance_derivada(v,w):
    return [func(w,i,v) for i in range(len(w))]


def first_principal_component(X):
    """
        retorna a primeira componente para o cojunto de dados
    """

    chute = [1 for _ in X[0]]

    tamless = maximize_batch(
        partial(direcional_variance_data,X),
        partial(direcional_variance_gradient_data,X),
        chute
    )

    return direction(tamless)


def first_principal_component_sthocastic(X):
    """
        retorna a componente principal para aquele conjunto de dados, usando descida do gradiente stochastica
    """

    chute = [1 for _ in X[0]]

    tamless = maximize_stochastic(
        lambda x,_,w: directional_variance(x,w),
        lambda x,_,w : direcional_variance_gradient(x,w),
        X,
        [None for _ in X[0]],
        chute
    )

    return direction(tamless)



def project(v,w):
    """
        retorna a projeção de v em w, mas note que estamos multiplicando
        o tamanho da projeção pelo vetor de direção, para remover
        a componente de v
    """

    tam = dot(v,w)

    return scalar_multiply(tam,w)

def remove_projection_vector(v,w):
    """
        remove uma componente principal de um vetor, a componente principal
        é w
    """

    return vector_subtract(v,project(v,w))

def remove_projection_dataset(X,w):
    """
        remove uma componente principal de um conjunto de dados linha
        a linha
    """
    return [remove_projection_vector(x,w) for x in X]


def principal_component_analysis(X, num_components):
    """
        retorna as n componentes principais para um cojuntos de dados
    """

    X = de_mean_matriz(X)

    com = []

    for _ in range(num_components):
        comp = first_principal_component(X)
        X = remove_projection_dataset(X,comp)
        com.append(comp)

    return com

def transform_vector(v,w):
    """
        retorna um novo vetor com a dimensionalidade reduzida
    """
    return [dot(v,wi) for wi in w]

def transform_data(X,num_components):
    """
        retorna um novo dataset com a dimensionalidade reduzida,
        note que reduzimos a dimensionalidade aqui nessa função mesmo
    """

    components = principal_component_analysis(X,num_components)

    print(components)

    return [transform_vector(x,components) for x in X]

