import random


def split_data(data, prob):
    """
        recebe um conjunto de dados e divide eles em dois conjuntos,
        um de treino e um de testes baseado na probabilidade especificada
    """

    results = [],[]

    for x in data:
        results[0 if random.random() < prob else 1].append(x)
    
    return results

def train_test_split(x,y, test_prob = 0.3):
    """
        divide os dados em xtreino, xteste, ytreino, yteste.
        ou seja, cojuntos de entradas e saidas pra os cojuntos
        de treino e teste
    """

    data = zip(x,y)

    train, test = split_data(data,1 - test_prob)


    xtrain, ytrain = zip(*train)

    xtest, ytest = zip(*test)

    return xtrain, xtest, ytrain, ytest

def accuracy(tp, fp, fn, tn):
    """
        retorna a medida de acuracia, mas lembre-se

           vp     vn
        ______________
    hp  |__tp__|__fp__|
    hn  |__fn__|__tn__|
    """

    corretos = tp + tn
    total = tp+fp+fn+tn

    return corretos / total

def precision(tp,fp,fn,tn):
    """
        retorna o quão precisas nossas previsões positivas eram

           vp     vn
        ______________
    hp  |__tp__|__fp__|
    hn  |__fn__|__tn__|
    """

    return tp / (tp + fp)

def recall(tp,fp,fn,tn):
    """
        retorna a fração dos positivos que nosso modelo acertou

        vp     vn
        ______________
    hp  |__tp__|__fp__|
    hn  |__fn__|__tn__|
    """

    return tp / (tp + fn)

def f1_socre(tp,fp,fn,tn):
    """
        retorna a media harmonica entre a precisão e o recall

        vp     vn
        ______________
    hp  |__tp__|__fp__|
    hn  |__fn__|__tn__|
    """

    preci = precision(tp,fp,fn,tn)

    reca = recall(tp,fp,fn,tn)

    return 2 * preci * reca / (preci + reca)