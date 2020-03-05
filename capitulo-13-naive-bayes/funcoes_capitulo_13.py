import re
from collections import defaultdict
import math


def tokenize(message):
    """
        tokenizamos nossa mensagem e retornamos um set de palavras válidas
    """

    message = message.lower()

    all_words = re.findall("[a-z0-9']+",message)

    return set(all_words)


def count_words(training_set):
    """
        retorna um dicionario onde a chave é a palavra e o valor é uma lista contendo a quantidade de vezes que
        ela aparece nas mensagens spam ou não spam
    """

    dic = defaultdict(lambda: [0,0])

    for message, is_spam in training_set:
        for word in tokenize(message):
            dic[word][0 if is_spam else 1] += 1
    
    return dic



def word_probablities(dici, cont_spam, cont_n_spam,min_count = 0, k = 0.5):
    """
        retorna uma tripla onde

        (w , P(w | S), P(w | ¬S)) e w é palavra
    """

    return [(w,
            (k + spam) / (2*k + cont_spam),
            (k + n_spam) / (2*k + cont_n_spam))
            for w,(spam,n_spam) in dici.items()
            if spam + n_spam > min_count
    ]

def spam_probability(wor_probs, message):
    """
        retorna a probabilidade de uma messagem ser spam
    
        ela é calculada na forma de:

        P(w1 | S)P(w2 | S)...P(wn | S) / (P(w1 | S)P(w2 | S)...P(wn | S) + P(w1 | ¬S)P(w2 | ¬S)...P(wn | ¬S)

        note que assim o teorema de bayes está imcompleto, faltando no numerador P(S) e no denominador P(S) e P(¬S)
         
        estamos desconsiderando pois assumimos que nossos dados são balanceados ou seja 50% spam e 50% n spam
    """

    token = tokenize(message)

    prob_is_spam = prob_is_not_spam = 0.0

    for w, p_spam, p_n_spam in wor_probs:

        if w in token:
            prob_is_spam += math.log(p_spam)
            prob_is_not_spam += math.log(p_n_spam)
        else:
            prob_is_spam += math.log(1 - p_spam)
            prob_is_not_spam += math.log(1 - p_n_spam)

    prob_is_spam = math.exp(prob_is_spam)
    prob_is_not_spam = math.exp(prob_is_not_spam)

    return prob_is_spam / (prob_is_spam + prob_is_not_spam) # a magica aq po

class NaiveBayesClassifier:

    """
        classificador baseado no teorema de bayes
    """
    
    def __init__(self, k  = 0.5):
        """
            k é suavizador, está por default em 0.5
        """
        self.k = k
        self.word_probs = []

    def train(self, data, min_count = 0):
        """
            treina o classificador, os dados tem que vir na forma de (messagem (string), is_spam (boolean))
        """

        len_spam = sum([1 for message, is_spam in data if is_spam])
        len_not_spam = len(data) - len_spam

        palavras_contadas = count_words(data)

        self.word_probs = word_probablities(palavras_contadas,len_spam,len_not_spam,min_count,self.k)


    def classify(self,message):
        """
            classifica nossa mensagem como spam ou não spam
        """

        return spam_probability(self.word_probs,message)

    def most_prob(self):
        """
            retorna as palavras que tem mais probabilidade de ser spam dado que ela aparece na mensagem
        """

        lista = [(w,pp / (pp + pn)) for w,pp,pn in self.word_probs]

        lista = sorted(lista,key=lambda p: p[1])

        return lista


