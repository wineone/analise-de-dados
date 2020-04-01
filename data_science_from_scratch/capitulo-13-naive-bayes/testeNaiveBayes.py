import glob, re
import codecs
import sys
sys.path.append("../capitulo-11-aprendizado-de-maquina")
from funcoes_capitulo_11 import *
import random
from funcoes_capitulo_13 import *
from collections import Counter

path = "spam/*/*"

data = []

for arquivo in glob.glob(path):
    
    is_spam = "ham" not in arquivo

    with codecs.open(arquivo,"r",encoding='utf-8',errors='ignore') as f:

        for line in f.readlines():

            if line.startswith("Subject: "):
                
                line = re.sub("^Subject: ","",line).strip()

                data.append((line,is_spam))

random.seed(0)

train,test = split_data(data,0.75)

print(len(train),len(test))

model = NaiveBayesClassifier(0.4)

model.train(train)

respostas = [(origi,model.classify(menssagem) > 0.5) for menssagem, origi in test]

saidas = Counter(respostas)

for i in saidas.items():
  print(i)


lista = model.most_prob()

print("palavras com mais cara de spam:")
for i in lista[-5:]:
    print(i)

print("palavras com menos cara de spam")
for i in lista[:5]:
    print(i)
  
