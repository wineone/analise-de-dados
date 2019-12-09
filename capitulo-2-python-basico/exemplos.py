from __future__ import division # módulo para a divisão ser quebradinha

from funcoes_capitulo_2 import *
from collections import defaultdict
from collections import Counter


# funções 

print("dobro de 2,",double(2))

print("aplica a 5,",apply_func_5(double))

print("minus,",minus())

print("minus,",minus(b=10))

print("dobro em lambda: ", apply_func_5(lambda x: x * 2) )


# strings 

print("\ttab ai") # uso do caractere \ como especial

print(r"\t") # uso do r antes da string para dizer que eh uma string bruta

# excecoes

try:
    0 / 0
except ZeroDivisionError:
    print("tentasse dividir por zero viss")

# listas


lista = list(range(10))

print("ultimos 3 elementos da lista,",lista[-3:]) # pegando os ultimos 3 elementos

x = lista # mesma lista
y = lista[:] # slice de todos os elementos, mas note que é a copia da lista

lista.extend([1,2,3]) # extende a lista que nós temos

print("aumentou?", y)
print("com certeza aumentou,", x)

_, x = [1,2] # variavel anônima

print("x,",x)

# tuplas

my_tuple = 3,4

try:
    my_tuple[0] = 5
except TypeError:
    print("n pode mudar tupla po")

s,p = sum_product(3,5)

print("a soma e produto de 3,5 é:",s,p)

# dicionario 

dic = {"matheus":"EMPOLGADO DMEAAAAISSS","uau":"WAAAAW"}


try:
    dic["numtem"] # um dicionario retorna uma exceção quando voce tenta acessar uma posição que não existe
except KeyError:
    print("po num tem essa chave neh")


print("matheus" in dic) # o operador in usado para dicionario verifica se existe alguma chave com aquele valor

print("numsei" in dic)


# o metodo get retorna o valor default quando nao existe a key com aquele valor

print(dic.get("numsei",":("))
print(dic.get("matheus",":("))
print(dic.get("numsei")) # e none quando nao eh passado nada


# metodos importantes para o dic


print(dic.keys()) # retorna uma lista com as chaves
print(dic.values()) # retorna uma lista com os valores
print(dic.items()) # retorna uma lista com os pares (key,value)

# default dic, ele é um dicionario que não reclama quando voce tenta adicionar um valor que nao existe


pal = ["matheu", "aa","ddd","aa","ddd","uauauau","matheu","digai ohm"]


dicionario = defaultdict(lambda : 0) # sempre que não existir uma chave, ele adiciona o retorno dessa função. e depois executa sua tarefa

for i in pal:
    dicionario[i] += 1

print(dicionario)


dici2 = defaultdict(dict) # retorna um {}

nomes = ["matheus","rafuela","joao"]

idades = [20,18,99]

reais = [1000,10000,10]

for a,b,c in zip(nomes,idades,reais): # criando objetos completos apenas com um for, genial
    dici2[a]["idade"] = b
    dici2[a]["reais"] = c

print(dici2)


# Counter, faz a contagem de frequencia de elementos num documento


lista = [1,6,5,8,7,6,7,8,9,0,65,4,5,3,4,5,6,3,2,1]

contador = Counter(lista)

print(contador)


print(contador.most_common(4)) # retorna uma lista ordenada de um par (chave,valor) dos mais comuns do contador

# conjuntos

# sets são bons pois são implementados com uma arvore, o que o torna o in muito rapido

lista = [1,2,3,1,2,3]

lista_set = set(lista)

print(lista_set)

print("teste de veracidade para set,",3 in lista_set)

print("teste falso de veracidade,",4 in lista_set)


# veracidade 

x = None

print("teste de igualdade com none,",x is None)


# funções any e all

# equivalente a um and

print("função all, retorna true se todos os elementos são true,",all([1,2,3,[12,4],{0:99},set([1,34])]))

print("função all, retorna true se todos os elementos são true, com um falso,",all([1,2,3,[],{0:99},set([1,34])]))

# equivalente a um or

print("função any, se tem algum true,",any([0,0,0,1]))

print("função any, se tem algum true,",any([0,0,0,{}]))

# ordenação

lista = [(1,10),(2,9),(3,5),(7,99)]

nova = sorted(lista, key = lambda a: a[1]) # ordenação com função passada por padrão

print(nova)

# compreensão de dicionario

dici = {x : x * x for x in range(10)}

print("compreenção de dicionario,",dici)


# geradores preguiçosos

def lazy_range(t): #como isso funciona? kk realmente n sei
    n = 0
    while n < t:
        yield n
        n += 1

print(list(lazy_range(10)))


# aleatoriedade

import random


lista = [random.random() for _ in range(10)]


print("lista com numeros aleatorios entre 0 e 1,",lista)

random.seed(10)

print(random.random())

random.seed(10)

print(random.random())

lista = [1,2,3,4,5]

random.shuffle(lista)

print(lista)

print(random.sample(lista,3)) # pega valores de uma lista se repetição


# poo

s = Set([1,2,3,4,4,4])

print("nosso set implementado,",s)

s.adiciona(5)
s.remove(4)

print("nosso set implementado,",s) #tudo funcionando ceritinho ohm

print("tem?",s.contains(2))




# ferramentas funcionais


# partial, ela pega uma função e aplica os parametros passados pra ela na ordem e retorna uma função nova

from functools import partial

def exp(base,exp):
    return base**exp


pot2 = partial(exp,2)

print(pot2(3))


# map, alternativa para compreesão de lista, pega uma função e aplica para todos os elementos e retorna uma nova lista


lista = [1,2,3,4,5]

nova = map(lambda x: x *2, lista)

double  = partial(map,lambda x : x*2)

print(list(double(lista)))

# filter, uma compreesão com um if

lista = [1,2,3,4,5,6]

nova = filter(lambda x : x%2, lista)

impar = partial(filter,lambda x: x%2)

print(list(impar(nova)))

# reduce combina todos os elementos de uma lista de acordo com uma função

from functools import reduce

lista = [1,2,3,4,5,6]

nova = reduce(lambda x,y: x+y, lista)

print(nova)


# enumeração


lista = [1,2,99,4,5,6,7]

print(list(enumerate(lista)))

for ind, ele in enumerate(lista):
    print(ind,ele)

for ind, _ in enumerate(lista):
    print(ind,end="")
print()

# zip, compacta duas listas ou mais em tuplas por seus elementos


lista1 = [1,2,3,4,5]

lista2 = [2,3,4,5,6]

lista3 = [3,4,5,6,7]

zipado = list(zip(lista1,lista2,lista3))

print(list(zip(*zipado)))



print(add(*[1,2]))



#args e kargs

print(magic(1,2,3,4,key=99,key1=88))

k = double_func(lambda x,y,z: x+y+z)

print(k(1,2,3))

