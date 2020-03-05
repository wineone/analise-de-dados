from funcoes_capitulo_10 import *
import random
import sys
sys.path.append("../capitulo-6-probabilidade")
from funcoes_capitulo_6 import *


# ambas as distribuições tem média 0 e desvio padrão em torno de 57

TAM = 100000

uni = [random.randint(-100,101) for _ in range(TAM)]

nor = [57 * inverse_normal_cdf(random.random()) for _ in range(TAM)]

plot_histogram(uni,10,"histograma uniforme")

plot_histogram(nor,10,"histograma normal")