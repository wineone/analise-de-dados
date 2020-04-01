from matplotlib import pyplot as plt


# graficos de linha são indicados para mostrar a variação de um dados conforme o tempo



variancia = [1,2,4,8,16,32,64,128,256]

bias_squared = [256,128,64,32,16,8,4,2,1]

total_error = [x+y for x,y in zip(variancia,bias_squared)]

xs = [i for i,_ in enumerate(variancia)]

plt.plot(xs,variancia,"g-",label="variancia")
plt.plot(xs,bias_squared,"r-.",label="bias squared")
plt.plot(xs,total_error,"b:",label="erro total")

plt.xlabel("aumento do tamanho")
plt.ylabel("tamanho do aumento")
plt.title("error do modelo")
plt.legend()

plt.show()