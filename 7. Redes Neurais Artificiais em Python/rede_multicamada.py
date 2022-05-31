"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd
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

# ajuste dos pesos  
pesos_xor, i_xor = camada_ocultaI()
    
print('Pesos operador XOR:',[round(i, 4) for i in pesos_xor])
print('Iterações XOR:',i_xor)
