import numpy as np
import random

def sigmoid(z):
    """
        aplica a função sigmoid a uma entrada
    """

    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    """
        retorna a derivada da função sigmoid no ponto
    """
    return sigmoid(z) * (1 - sigmoid(z))

class Network:
    """
        classe para construir a rede neural
    """

    def __init__(self, sizes):

        self.num_layers = len(sizes)

        self.bias = [np.random.randn(y,1) for y in sizes[1:]] # a primeira camada não tem bias
        self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])] # liga a primeira camada com a segunda, a segunda com a terceira e etc

    
    def feed_foward(self, a):
        """
            faz a passagem entre nossos dados nas camadas da rede neural
        """
        for b,w in zip(self.bias,self.weights):
            a = sigmoid(np.dot(w,a) + b)
        
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):
        """
            faz o treinamento da rede neural usando mini_batch
        """
        training_data = list(training_data)
        n = len(training_data)
        print(n)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)
    
        for j in range(epochs):
            random.shuffle(training_data) # randomiza os dados
            mini_batches = [training_data[k: k + mini_batch_size] for k in range(0,n,mini_batch_size)] # separa em minibatches para treinar mais rapidamente

            for mini in mini_batches:
                self.update_mini_batch(mini,eta)

            if test_data:
                pass
                #print("%d : %d / %d"%(j,self.evaluate(test_data),n_test))
            else:
                print("epoca %d terminada"%j)

    def update_mini_batch(self,mini_batch, eta):
        """
            função que faz a atualização dos pesos de acordo com o mini batch e a taxa de aprendizagem
        """

        n_p = [np.zeros(m.shape) for m in self.weights]
        n_b = [np.zeros(m.shape) for m in self.bias]

        for x,y in mini_batch:
            delta_p, delta_b = self.backprop(x,y) 
            n_p = [p + dp for p, dp in zip(n_p,delta_p)]
            n_b = [b + db for b, db in zip(n_b,delta_b)]

        #print("variação dos pesos,\n",n_p)
        #print("variação dos bias\n",n_b)

        self.weights = [w + (eta / len(mini_batch)) * d_p for w,d_p in zip(self.weights,n_p)] # pesos são atualizados aq
        self.bias = [b + (eta / len(mini_batch)) * d_b for b, d_b in zip(self.bias, n_b)]

        #print("pesos\n",self.weights)
        #print("bias\n",self.bias)

    def backprop(self,x,y):
        """
            algoritmo de backpropagation para fazer nossa rede neural aprender
        """
        delta_w = [np.zeros(w.shape) for w in self.weights]
        delta_b = [np.zeros(b.shape) for b in self.bias]

        activation = x

        activations = [x] # saidas da rede com a sigmoid

        zs = [] # saidas da rede sem passar pela sigmoid


        # feed foward
        for w,b in zip(self.weights, self.bias):
            z = np.dot(w,activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        # atualização da ultima camada
        delta = self.cost_derivate(activations[-1],y) * sigmoid_prime(zs[-1]) # primeiro delta
        delta_b[-1] = delta
        delta_w[-1] = np.dot(delta,activations[-2].transpose())

        # atualização das camadas hidden
        for i in range(2,self.num_layers):
            z = zs[-i]
            dz = sigmoid_prime(z)
            delta = np.dot(self.weights[-i + 1].transpose(),delta) * dz
            delta_b[-i] = delta
            delta_w[-i] = np.dot(delta,activations[-i-1].transpose())

        return (delta_w,delta_b)
    

    def cost_derivate(self,out, y):
        """
            o custo da função de erro no ultimo neuronio
        """
        return (y-out)
    


    def printa_pesos(self):
        print("bias")
        print(self.bias)
        print("pesos")
        print(self.weights)