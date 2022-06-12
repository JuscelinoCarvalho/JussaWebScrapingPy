import numpy as np 

class clsTestes(object):
    """
        Classe criada por Juscelino A. de Carvalho 
        Sábado 31 de Julho de 2021   13:18
       
        Esta Classe é destinada apenas para pequenos testes de códigos.
    """


    def __init__(self):
        pass

    prices = np.array([200, 400, 300, 100, 800, 500, 1000, 99, 95, 1.23, 45.3])
    
    print((prices > 500).any(axis = 0) )

    L = ['a','b','c','d']
    print("".join(L))

