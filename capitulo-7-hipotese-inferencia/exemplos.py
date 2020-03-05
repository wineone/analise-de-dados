from funcoes_capitulo_7 import *


# testes com as funções de normal

print("a probabilidade abaixo de 2,",normal_probability_below(2))
print("a probabilidade acima de 0,",normal_probability_above(0))
print("a probabilidade entre -2~2 com desvio de 0.5,",normal_probability_between(-2,2,desvio=0.5))

# teste com os limites ao redor da média

media_bin, des_bin = normal_aproximation_to_binomial(1000,0.5)

lo,hi = normal_two_sided_bounds(0.95,media_bin,des_bin)

print("limite inferior para rejeitarmos h0,",lo)
print("limite superior para reijeitarmos h1,",hi)

# testes com p value

print("vamos ver o valor para 531 para o teste anterior,",two_sided_p_value(531,media_bin,des_bin),", note que bate")
print("vamos verificar se a moeda é viciada para um unico lado,",upper_p_value(526,media_bin,des_bin))

# intervalos de confiança

tentativas = 1000
caras = 540

proporcao = caras / tentativas

media = proporcao
des = math.sqrt(media * (1 - media)) / math.sqrt(tentativas)

print("o intervalo de confianca é,",intervalo_de_confianca(media,media,des))


# executando um teste a / b


na = 2000
Na = 10000

nb = 1700
Nb = 10000

estimadoA = estimated_values(na,Na)
estimadoB = estimated_values(nb,Nb)

print("valores estimados para a,",estimadoA)
print("valores estimados para b,",estimadoB)

print("o p value para saber se as duas proporcoes são iguais,",valor_p_teste_ab(na,Na,nb,Nb))
