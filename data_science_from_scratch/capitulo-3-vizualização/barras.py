# graficos de barra, usado para comparar resultados entre um conjunto de dados independente

from matplotlib import pyplot as plt

filmes = ["benhur","annie-hall","casablanca","ganhdi","west side history"]

oscars = [10,15,7,9,8]

plt.bar(filmes,oscars)

plt.show()