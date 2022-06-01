"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

# feedforward

import pandas as pd
import numpy as np
from NeuralNetwork import sigmoid_function, camada_ocultaI

lista_x = [0, 0, 1, 1]
lista_y = [0, 1, 0, 1]
entradas_xy = [[lista_x[i],lista_y[i]] for i in range(len(lista_x))]

# operador XOR esperado
esperados_xor = [0,1,1,0]

# tabela verdade
OP = pd.DataFrame({
    'x1':lista_x, 
    'x2':lista_y, 
    'classe_XOR':esperados_xor
    })

print(OP)

# camada de entrada para camada oculta
pesos0 = [[-0.424, -0.740, -0.961], 
          [0.358, -0.577, -0.469]]
# camada oculta para camada de saída
pesos1 = [-0.017, -0.893, 0.148]

epocas = 100

# ajuste dos pesos  
a = camada_ocultaI(epocas, entradas_xy, pesos0, pesos1)
    
#print('Pesos operador XOR:',[round(i, 4) for i in pesos_xor])
#print('Iterações XOR:',i_xor)
