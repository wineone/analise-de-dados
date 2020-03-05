from funcoes_capitulo_8 import *
from matplotlib import pyplot as plt

x = list(range(-10,10))

plt.plot(x,[derivate_square(i) for i in x],'rx',label = "derivada original")
plt.plot(x,[derivate(square,i) for i in x],'b+',label = "imitação da derivada")

plt.legend()

plt.show()