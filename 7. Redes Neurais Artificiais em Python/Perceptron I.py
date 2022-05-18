# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""
from NeuralNetwork import soma, step_function

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0.0] # ou sinapses

s = soma(entradas, pesos)
r = step_function(s)

print(f'Soma: {s}')
print(f'Resposta: {r}')
