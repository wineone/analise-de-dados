from funcoes_capitulo_17 import *


print("teste da entropia,",entropy([0.1,0.1,0.01,0.80,0.001])) # note que é uma soma, então é bom se ligar o que entropia pouca quer dizer depende do conjunto de dados

print("entropia num conjunto de dados,",data_entropy([(1,1),(1,1),(1,2),(1,1),(1,2)]))

inputs = [
    ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},   False),
    ({'level':'Senior','lang':'Java','tweets':'no','phd':'yes'},  False),
    ({'level':'Mid','lang':'Python','tweets':'no','phd':'no'},     True),
    ({'level':'Junior','lang':'Python','tweets':'no','phd':'no'},  True),
    ({'level':'Junior','lang':'R','tweets':'yes','phd':'no'},      True),
    ({'level':'Junior','lang':'R','tweets':'yes','phd':'yes'},    False),
    ({'level':'Mid','lang':'R','tweets':'yes','phd':'yes'},        True),
    ({'level':'Senior','lang':'Python','tweets':'no','phd':'no'}, False),
    ({'level':'Senior','lang':'R','tweets':'yes','phd':'no'},      True),
    ({'level':'Junior','lang':'Python','tweets':'yes','phd':'no'}, True),
    ({'level':'Senior','lang':'Python','tweets':'yes','phd':'yes'},True),
    ({'level':'Mid','lang':'Python','tweets':'no','phd':'yes'},    True),
    ({'level':'Mid','lang':'Java','tweets':'yes','phd':'no'},      True),
    ({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'},False)
]

print("\nprimeira rodada, para todos:\n")

for key in ['level','lang','tweets','phd']:
    print(key,partition_entropy_by(inputs,key))

# level representou a menor entropia da separação

print("\nsegunda rodada, sem level, já que ele foi o menor:\n")

nova_particao = [(atrib,label) for atrib,label in inputs if atrib['level'] == "Senior"]


for key in ['lang','tweets','phd']:
    print(key,partition_entropy_by(nova_particao,key))


## juntando tudo

arvore = build_tree_id3(inputs)


print(classify(arvore,({'level':"Junior","lang":"Java","tweets":"yes","phd":"no"})))

print(classify(arvore,{"level":"Senior"}))

print(classify(arvore,{"level":"estagiario"}))

print(classify(arvore,{'level':'Junior','lang':'Python','tweets':'no','phd':'yes'}))


model = randomFlorestClassify(3,15)

model.train(inputs)

print(model.predict({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'}))