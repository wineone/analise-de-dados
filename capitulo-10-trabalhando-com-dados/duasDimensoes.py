from matplotlib import pyplot as plt
from funcoes_capitulo_10 import *
import sys
sys.path.append("../capitulo-6-probabilidade")
sys.path.append("../capitulo-5-estatistica")
from funcoes_capitulo_6 import *
from funcoes_capitulo_5 import *
from collections import Counter



TAM = 10000

xs = [random_normal() for _ in range(TAM)]
ys1 = [-x + random_normal()/2 for x in xs]
ys2 = [x + random_normal()/2 for x in xs]

print("correlação entre xs, ys1,",correlation(xs,ys1))
print("correlação entre xs, ys2,",correlation(xs,ys2))

plt.scatter(xs,ys1,marker = ".",label="ys1",alpha=0.3)
plt.scatter(xs,ys2,marker =".",label="ys2",alpha=0.3)

plt.legend()

plt.ylim([-6,6])

plt.show()