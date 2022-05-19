# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd

lista_x = [0, 0, 1, 1]
lista_y = [0, 1, 0, 1]
resultados = []

for i in range(len(lista_x)):
    resultado = operador_E(lista_x[i], lista_y[i])
    resultados.append(resultado)
    
OP_E = pd.DataFrame({
    'x1':lista_x, 
    'x2':lista_y, 
    'classe':resultados})

print(OP_E)
