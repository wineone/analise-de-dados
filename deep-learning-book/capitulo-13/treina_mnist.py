from funcoes_capitulo_13 import *


net = Network([784,15,10])

dados = []

with open("dataset/datset.txt","r") as f:
	for line in f.readlines():
		dados.append(eval(line))


print("comeco do treinamento")

treinamento = dados[:19000]
teste = dados[19000:]

net.SGD(treinamento,1,100,0.5)

acertos = 0
erros = 0

for x,y in teste:
	sai = net.feed_foward(x)
	s = 0
	for i in range(10):
		if y[i][0] == 1:
			s = i
	if sai[s][0] > 0.8:
		acertos += 1
	else:
		erros += 1

print(acertos / (acertos + erros))



