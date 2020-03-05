import math
from collections import Counter,defaultdict
from functools import partial
import random

def entropy(classes_distribution):
    """
        retorna a entropia de um conjiunto de dados de acordo com as 
        proporções das categorias, note que quando estão pouco divididos
        a entropia será perto de zero
    """

    return sum([-p * math.log(p,2) for p in classes_distribution if p]) # if p ignora o caso de 0

def class_probabilities(labels):
    """
        retorna as probabilidades de cada label no conjunto de dados
    """
    dic = Counter(labels)
    tam = len(labels)
    return [cont / tam for cont in dic.values()]

def data_entropy(labeled_data):
    """
        retorna a entropia de um conjunto de dados que cada linha tem a forma (values, label)
    """

    labels = [label for _,label in labeled_data]

    probs = class_probabilities(labels)

    return entropy(probs)

def subset_entropy(subsets):
    """
        retorna a entropia de subsets como uma soma ponderada pelos tamanhos dos subsets.

        dado um conjunto S dividido em proporções p1,p2,p3,..,pn

        a entropia vai ser definida como

        H = p1 * H(S1) + p2 * H(S2) + .. + pn* H(Sn)

        onde cada Sn é um subset
    """

    tamanho = sum(len(sub) for sub in subsets)

    return sum([(len(sn) / tamanho) * data_entropy(sn) for sn in subsets])

def partition_by(inputs, atribute):
    """
        constroi um dicionario com base nos valores diferentes de um atribuito, vai ser usado para 
        computar a entropia de um nó da arvore
    """

    grupos = defaultdict(lambda : [])

    for inp in inputs:
        valor = inp[0][atribute]
        grupos[valor].append(inp)
    return grupos

def partition_entropy_by(inputs, atribute):
    """
        retorna a entropia resultante de particionar o grupo de dados por certo atributo,
        esse numero é calculado como a soma ponderada de cada subgrupo resultante do particionamento
    """
    return subset_entropy([sub for sub in partition_by(inputs,atribute).values()])



def build_tree_id3(inputs, atributes = None):
    """
        constroi a árvore com base no algoritmo id3 que através de maneira gulosa escolhe
        o atributo com a menor entropia.
    """

    if atributes is None:
        atributes = inputs[0][0].keys() # pega todas as keys para o primeiro passo de construir a árvore

    num_inputs = len(inputs)
    num_true = len([label for _,label in inputs if label == True])
    num_false = num_inputs - num_true

    # casos base

    if num_false == 0:
        return True
    
    elif num_true == 0:
        return False

    if not atributes: 
        return num_true >= num_false

    
    # se não foi nenhum caso base

    best_atribute = min(atributes,key=partial(partition_entropy_by,inputs))

    partitions = partition_by(inputs,best_atribute)

    new_cadidates = [a for a in atributes if a != best_atribute]

    sub_tree = {key: build_tree_id3(value,new_cadidates) for key,value in partitions.items()}

    sub_tree[None] = num_true >= num_false

    return (best_atribute,sub_tree)

def classify(tree, inp):
    """
        retorna uma classificação de acordo com a árvore de descisão
    """

    if tree in [True, False]:
        return tree
    

    atribute, subtree = tree

    resposta = inp.get(atribute)

    if resposta not in subtree:
        resposta = None
    
    saida = subtree[resposta]

    return classify(saida,inp)



class randomFlorestClassify:


    def __init__(self, tam_split, quant_arvores):

        self.tam_split = tam_split

        self.quant_arvores = quant_arvores

        self.trees = None

    def train(self, inputs):

        self.trees = [self.class_build_tree_id3(inputs) for _ in range(self.quant_arvores)]


    def predict(self, inp):

        votos = [classify(a,inp) for a in self.trees]

        d = Counter(votos)

        return d.most_common(1)[0]
    
    def class_build_tree_id3(self,inputs, atributes = None):
        """
            constroi a árvore com base no algoritmo id3 que através de maneira gulosa escolhe
            o atributo com a menor entropia.
        """

        if atributes is None:
            atributes = inputs[0][0].keys() # pega todas as keys para o primeiro passo de construir a árvore

        num_inputs = len(inputs)
        num_true = len([label for _,label in inputs if label == True])
        num_false = num_inputs - num_true

        # casos base

        if num_false == 0:
            return True
        
        elif num_true == 0:
            return False

        if not atributes: 
            return num_true >= num_false

        
        # se não foi nenhum caso base

        if len(atributes) > self.tam_split:
            atributes = random.sample(atributes,self.tam_split)

        best_atribute = min(atributes,key=partial(partition_entropy_by,inputs))

        partitions = partition_by(inputs,best_atribute)

        new_cadidates = [a for a in atributes if a != best_atribute]

        sub_tree = {key: build_tree_id3(value,new_cadidates) for key,value in partitions.items()}

        sub_tree[None] = num_true >= num_false

        return (best_atribute,sub_tree)