from funcoes_capitulo_5 import *

# tendencias centrais

dados = [1,1,2,2,3,3,4,5,6,7,8,9,10,11,12]


print("a média dos dados é,",mean(dados))

print("a mediana é,",median(dados))

print("quantil de 50,",quantile(dados,0.5))

print("a moda do conjunto de dados é,",mode(dados))

# dispersão

print("amplitude,",amplitude(dados))

#print("diferenca array",diff_media(dados))

print("variancia dos dados,",variance(dados))

print("desvio padrão dos dados,",standard_deviation(dados))

print("distancia interquartilica,",interquartile_range(dados))

# covariancia

a = [1,2,3,4,5]

b = [4,5,6,7,8]

c = [9,8,7,6,5]

d = [2,5,6,7,9]

f = [6,8,35,67,99]

print("a covariancia das variaveis a e b,",covariance(a,b))

print("covariancia entre a e c",covariance(a,c))

print("correlação entre a e b",correlation(a,b))

print("correlação entre a e c",correlation(a,c))

print("correlação entre d e f",correlation(d,f))

# paradoxo de simpson


