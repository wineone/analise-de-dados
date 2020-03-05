from matplotlib import pyplot as plt
from funcoes_capitulo_6 import *



xs = [i / 10 for i in range(-50,50)]


plt.plot(xs,[normal_pdf(i) for i in xs],'-',label="u = 0, des = 1")
plt.plot(xs,[normal_pdf(i,des=3) for i in xs],'--',label="u = 0, des = 3")
plt.plot(xs,[normal_pdf(i,des=0.5) for i in xs],':',label="u = 0, des = 0.5")

plt.title("plot de algumas curvas normais")

plt.legend()

plt.show()
