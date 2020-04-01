from funcoes_capitulo_6 import *

# experimento para verificar as probabilidades condicionais

both = 0
one = 0
older = 0


tam = 10000

for i in range(tam):
    f1 = random_kid()
    f2 = random_kid()

    if f2 == "girl":
        older += 1
    if f2 == "girl" or f1 == "girl":
        one += 1
    if f1 == "girl" and f2 == "girl":
        both += 1

print(both,one,older)

print("as duas dado que a mais velha é menina: ",both / older)

print("as duas dado que é uma é menina, ",both / one)


# variaveis aleatórias

n = 0.2420

print("o inverso para %.1f é: %.1f"%(n,inverse_normal_cdf(n)))