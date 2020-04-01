from matplotlib import pyplot as plt

# graficos de dispersão são bons para verificar a relaçao entre duas variáveis

friends = [70,65,72,63,71,64,60,64,67]
time = [175,170,205,120,220,130,105,145,190]
anota = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,time)

for label,amigo,minutes in zip(anota,friends,time):
    plt.text(amigo+0.2,minutes+1,label)

plt.show()