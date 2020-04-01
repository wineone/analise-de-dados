from funcoes_capitulo_10 import *
import csv
from matplotlib import pyplot as plt

data = []

with open("teste.csv","r") as f:
    reader = csv.reader(f)
    for line in parse_data(reader,[int,None,float]):
        data.append(line)

print(data)


data = [
    {"a":"10","b":"0.77"},
    {"a":"10","b":"0.1"},
    {"a":"77","b":"0.9"},
    {"a":"10","b":"0.77"},
    {"a":"10","b":"0.009"},
    {"a":"10","b":"0.77"},
    {"a":"10","b":"0.77"},
]

parsers = {"a":int,"b":float}

saida = []

for i in parse_data_dict(data,parsers):
    saida.append(i)

print(saida)

print("lista de valores extraidos do dic,",list(pluck("a",data)))

print("agrupando por valor 10,",group_by(lambda row: row["a"],saida,lambda rows: sum(pluck("b",rows))))

# redimensionando os dados

data2 = [
    [63,160,150], # a
    [67,170.2,160], # b
    [70,177.8,171] # c
]

print("a to b inche",distance([63,150],[67,160]))
print("a to c inche",distance([63,150],[70,171]))
print("b to c inche",distance([67,160],[70,171]))

print()

print("a to b meters",distance([160,150],[170.2,160]))
print("a to c meters",distance([160,150],[177.8,171]))
print("b to c meters",distance([170.2,160],[177.8,171]))


print("redimensionado")

dados = rescale(data2)

print("a to b inche",distance([-1.2787240261820139, 1.1624763874381911],[-1.2798336846655038, 1.1609919853751347]))
print("a to c inche",distance([-1.2787240261820139, 1.1624763874381911],[-1.2048492152215322, 1.2437153189383536]))
print("b to c inche",distance([-1.2798336846655038, 1.1609919853751347],[-1.2048492152215322, 1.2437153189383536]))


print()


print("a to b meters",distance([0.11624763874381763, 1.1624763874381911],[0.11884169929036524, 1.1609919853751347]))
print("a to c meters",distance([0.11624763874381763, 1.1624763874381911],[-0.03886610371682469, 1.2437153189383536]))
print("b to c meters",distance([0.11884169929036524, 1.1609919853751347],[-0.03886610371682469, 1.2437153189383536]))

print()

# redução da dimensionalidade 

data = [
    [2.7,3.3],
    [3.6,3.4],
    [4.2,3.45],
    [5,3.6],
    [3.7,4.2],
    [4.5,4.2],
    [3.1,4.7],
    [4,5.1],
    [5.1,5],
    [5.6,4.2],
    [5,5.9],
    [5.8,5.2],
    [6.5,4.7],
    [6.7,5.7],
    [5.9,6.2],
    [6.7,6.5],
    [7.2,5.2],
    [7.8,4.9],
    [8,6],
    [7.3,6.2],
    [8.2,6.9]
]

a = transform_data(data,1)

for i in a:
    print(i)

### CAPITULO 10 TERMINOU CARAYYY A MEU DEUS 1 SEMANA SÓ NO ULTIMO TOPICO TO MALUXOOOO