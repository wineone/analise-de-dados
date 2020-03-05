from keras.datasets import mnist


(xtrain, ytrain), (xtest, ytest) = mnist.load_data()

saida = []

for i in range(20000):
	x = []
	for line in xtrain[i]:
		for i in line:
			x.append([i])
	y = [[0 if ytrain[i] != j else 1] for j in range(10)]
	saida.append((x,y))

	
with open("datset.txt","a") as f:
	for line in saida:
		f.write(str(line)+"\n")
