# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd

lista_x = [0, 0, 1, 1]
lista_y = [0, 1, 0, 1]

resultados_e = []
resultados_ou = []
esperados_e = []
esperados_ou = []

# operador E
for i in range(len(lista_x)):
    esperado_e = lista_x[i] and lista_y[i]
    esperados_e.append(esperado_e)
    
    esperado_ou = lista_x[i] or lista_y[i]
    esperados_ou.append(esperado_ou)
    
OP_E = pd.DataFrame({
    'x1':lista_x, 
    'x2':lista_y, 
    'classe_E':esperados_e,
    'classe_OU':esperados_ou})

print(OP_E)
