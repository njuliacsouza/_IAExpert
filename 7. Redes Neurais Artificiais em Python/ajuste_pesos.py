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
pesos_e = np.array(peso_inicial)
pesos_ou = np.array(peso_inicial)
erros_e = [10 for _ in range(len(lista_x))]
erros_ou = [10 for _ in range(len(lista_x))]
erros = erros_e + erros_ou
i = 0
    
while max(erros)>0.01:
    i += 1
    for i in range(len(lista_x)):
        resultado_e = (lista_x[i] * pesos_e[0]) + (lista_y[i] * pesos_e[1]) 
        resultado_ou = (lista_x[i] * pesos_ou[0]) + (lista_y[i] * pesos_ou[1]) 
        
        erro_e = esperados_e[i] - resultado_e
        erro_ou = esperados_ou[i] - resultado_ou
        erros_e[i] = erro_e
        erros_ou[i] = erro_ou
        
        if (erro_e > 0.001):
            pesos_e = pesos_e + (0.1 * lista_x[i]*erro_e)
        elif (erro_ou > 0.001):
            pesos_ou = pesos_ou + (0.1 * lista_x[i]*erro_ou)
    erros = erros_e + erros_ou
        
print('Pesos operador E:',pesos_e)
print('Pesos operador OU:',pesos_ou)
print('Iterações:',i)
