


def double(x):

    """
        essa função pega a entrada a multiplica por 2
    """
    return x * 2 


def apply_func_5(f):
    """
    aplica a função recebida por paramentro ao numero 5
    """
    return f(5)

def minus(a=0,b=55):

    """
    demonstração de como passar valores padrão para a função
    """

    return a-b

def sum_product(a = 1,b = 1):
    """
        retorna a soma e o produto de dois numeros nessa ordem
    """

    return a+b,a*b


class Set:

    """
        classe que usamos para representar um set, criada como exemplo do livro
    """

    def __init__(self, values = None):

        self.dict = {}

        if values is not None:
            for i in values:
                self.dict[i] = True
    
    def __str__(self):
        return "Set: " + str(self.dict.keys())

    def adiciona(self, valor):
        self.dict[valor] = True
    
    def remove(self, valor):
        del self.dict[valor]

    def contains(self,valor):
        return valor in self.dict



def add(x,y):
    return x+y


def magic(*args, **kargs):
    print("sem nome",args)
    print("com nome",kargs)

def double_func(f):

    def g(*args, **kargs):
        """
            recebe uma lista e descompacta e passa para a nova função
        """
        return 2*f(*args,**kargs)
    return g