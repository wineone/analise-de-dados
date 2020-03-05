from collections import Counter
import sys
sys.path.append("../capitulo-4-algebra-linear")
from funcoes_capitulo_4 import *


def majority_vote(labels):
    """
        faz uma contagem de votos e retorna o o que tem maior contagem
    """

    conta = Counter(labels)

    winner, winner_count = conta.most_common(1)[0]

    num_winner = sum([1 for count in conta.values() if count == winner_count])

    if num_winner == 1:
        return winner
    else:
        return majority_vote(labels[:-1])



def knn_classify(k, labeled_points, new_point):
    """
        classifica um novo dado de acordo com a votação dos dados que já tem
    """

    by_distance = sorted(labeled_points,key = lambda l: distance((l[0],l[1]),new_point)) # ordena pela menor distancia

    labels_for_vote = [nome for _,_,nome in by_distance[:k]] # retorna os k mais proximos

    winner = majority_vote(labels_for_vote) # conta o ganhador

    return winner

def testa(k,treino,teste):
    acertos = 0
    erros = 0

    print()
    print("para k == ",k,"temos")

    for line in teste:
        
        saida = knn_classify(k,treino,line)

        print(saida,line[2])

        if saida == line[2]:
            acertos += 1
        else:
            erros += 1
    
    return acertos / (acertos + erros)