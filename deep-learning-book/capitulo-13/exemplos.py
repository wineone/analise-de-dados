from funcoes_capitulo_13 import *


net = Network([2,2,1])


dados = [ 
          (np.array([[0],[0]]),np.array([0])),
          (np.array([[1],[0]]),np.array([1])),
          (np.array([[0],[1]]),np.array([1])),
          (np.array([[1],[1]]),np.array([0]))
         ]

print("0,0",net.feed_foward(np.array([[0],[0]])))
print("0,1",net.feed_foward(np.array([[1],[0]])))
print("1,0",net.feed_foward(np.array([[0],[1]])))
print("1,1",net.feed_foward(np.array([[1],[1]])))

net.SGD(dados,10000,1,0.1)


print("0,0",net.feed_foward(np.array([[0],[0]])))
print("0,1",net.feed_foward(np.array([[1],[0]])))
print("1,0",net.feed_foward(np.array([[0],[1]])))
print("1,1",net.feed_foward(np.array([[1],[1]])))


