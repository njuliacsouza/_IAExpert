# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd
import numpy as np
from NeuralNetwork import ajuste_pesos

lista_x = [0, 0, 1, 1]
lista_y = [0, 1, 0, 1]

# operador E, OU, esperado
esperados_e = [(lista_x[i] & lista_y[i]) for i in range(len(lista_x))]
esperados_ou = [(lista_x[i] | lista_y[i]) for i in range(len(lista_x))]

# tabela verdade
OP_E = pd.DataFrame({
    'x1':lista_x, 
    'x2':lista_y, 
    'classe_E':esperados_e,
    'classe_OU':esperados_ou})

print(OP_E)

# ajuste dos pesos  
erro_max = 0.001 
pesos_e, i_e = ajuste_pesos(lista_x, lista_y, esperados_e, erro_max)
pesos_ou, i_ou = ajuste_pesos(lista_x, lista_y, esperados_ou, erro_max)
    
print('Pesos operador E:',pesos_e)
print('Iterações E:',i_e)
print('Pesos operador OU:',pesos_ou)
print('Iterações OU:',i_ou)
