# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd
import numpy as np

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
peso_inicial = [0, 0]
pesos = np.array(peso_inicial)
erros_e = []

for i in range(len(lista_x)):
    resultado_e = (lista_x[i] * pesos[0]) + (lista_y[i] * pesos[1]) 
    erro = esperados_e[i] - resultado_e
    erros_e.append(erro)
    
    if erro > 0.001:
        pesos = pesos + (0.1 * lista_x[i]*erro)
        

print(pesos)
