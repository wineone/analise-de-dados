from matplotlib import pyplot as plt
from collections import Counter

notas = [11,44,66,77,87,98,76,79,65,45,67,78,65,43,56,78,98,100,100,0,0,0]

classifica = lambda x : (x // 10)* 10

histograma = Counter([classifica(i) for i in notas])

plt.bar(histograma.keys(),histograma.values(),6)

plt.xticks([i for i in range(0,101,10)])

plt.show()