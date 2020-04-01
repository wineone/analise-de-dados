from matplotlib import pyplot as plt
from funcoes_capitulo_6 import *

xs = [i / 10 for i in range(-50,50)]

plt.plot(xs,[normal_cdf(i) for i in xs],':',label="u = 0, des = 1")
plt.plot(xs,[normal_cdf(i,des=0.7) for i in xs],'--',label="u = 0, des = 0.7")

plt.legend()

plt.show()