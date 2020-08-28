from matplotlib import pyplot as plt


years = [1900,1910,1920,1930,1940,1950]
lucro = [10,20,10,30,40,20]


plt.plot(years,lucro,color="green",linestyle="solid",marker="o")

plt.title("lucro de uma empresa através dos anos")

plt.ylabel("lucro em bilhoes de dolares")

plt.show()


