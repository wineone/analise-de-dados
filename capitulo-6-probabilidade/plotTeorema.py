from matplotlib import pyplot as plt
from funcoes_capitulo_6 import *
from collections import Counter


tamExemplos = 10000

tamCada = 100

p = 0.5

media = p*tamCada

desvio = math.sqrt(p*(1-p)) * math.sqrt(tamCada)

lista = [media_bernoulli(tamCada,p) for _ in range(tamExemplos)]

dic = Counter(lista)

plt.bar(dic.keys(),[i for i in dic.values()],0.7)

xs = [i for i in range(30,70)]

plt.plot(xs,[normal_pdf(i,media,desvio) for i in xs],color="red")

plt.show()
