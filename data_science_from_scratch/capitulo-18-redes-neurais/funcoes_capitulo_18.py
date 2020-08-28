import math
import sys
sys.path.append("../capitulo-4-algebra-linear")
from funcoes_capitulo_4 import *


def sigmoid(x):
    """
        função sigmoid, lembrar da função logistica em regressão logistica.

        aqui ela será usada para suavizar a saida de um neuronio, quando soma ponderada
        do neuronio for muito positiva ele vai tender a 1, quando for negativa vai tender a 0
    """

    return 1 / (1 + math.exp(-x))


def neuron(pesos, entradas):
    """
        faz a soma ponderada dos pesos pela entrada, note que o vetor de entradas
        tem que ter um 1 ao final para colocar o viés (bias) e depois passa pela função sigmoid
    """
    return sigmoid(dot(pesos,entradas))



def feed_foward(network, inputs):
    """
        faz as multiplicacões das entradas pelas camadas ocultas e segue o caminho entre todas
        as camadas.
    """

    outputs = []

    for layer in network:

        inputs = inputs + [1]

        output = [neuron(pesos,inputs) for pesos in layer] # produzem as saidas que vão ser entradas para as proximas camadas

        outputs.append(output)

        inputs = output

    return outputs


def backpropagation(network, inputs, targets):
    """
        faz o algoritmo de backpropagation, não entendi, não vou mentir
        (mentira, entendi mais ou menos porem vou deixar pra estudar melhor quando ler o livro de deeplearning)
    """

    hidden_outputs,outputs = feed_foward(network,inputs)

    output_deltas = [output * (1 - output) * (output - target) for output,target in zip(outputs,targets)]

    for i,output_neuron in enumerate(network[-1]): # atualizando a camada de saida
        for j,p in enumerate(hidden_outputs + [1]):
            output_neuron[j] -= output_deltas[i] * p

    hidden_deltas = [hidden_output * (1 - hidden_output) * dot(output_deltas,[n[i] for n in network[-1]]) for i, hidden_output in enumerate(hidden_outputs)]


    