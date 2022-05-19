# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd

lista_x = [0, 0, 1, 1]
lista_y = [0, 1, 0, 1]

# operador E, OU, esperado
esperados_e = [(lista_x[i] and lista_y[i]) for i in range(len(lista_x))]
esperados_ou = [(lista_x[i] or lista_y[i]) for i in range(len(lista_x))]

    
OP_E = pd.DataFrame({
    'x1':lista_x, 
    'x2':lista_y, 
    'classe_E':esperados_e,
    'classe_OU':esperados_ou})

# ajuste dos pesos
resultados_e = []
resultados_ou = []

print(OP_E)
#print(pesos)
