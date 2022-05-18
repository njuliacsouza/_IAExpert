# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0.0] # ou sinapses

def soma(entradas: list, pesos: list) -> float:
    s = 0 # soma
    
    for i in range(len(entradas)):
        s += entradas[i] * pesos[i]
    
    return s

def step_function(soma: float) -> int:
    if (soma >= 1):
        return 1
    return 0


s = soma(entradas, pesos)
r = step_function(s)

print(f'Soma: {s}')
print(f'Resposta: {r}')
