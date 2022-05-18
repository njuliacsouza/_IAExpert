# -*- coding: utf-8 -*-
"""
IAExpert Academy - Redes Neurais Artificiais em Python
"""

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0.0] # ou sinapses

def soma(entradas: list, pesos: list) -> float:
    s = 0 # soma
    
    for i in range(len(entradas)):
        s += entradas[i] * pesos[i]
    
    return s

s = soma(entradas, pesos)
print(f'Soma: {s}')

def step_function(soma):
    if (soma >= 1):
        return 1
    return 0

r = step_function(s)

print(f'Resposta: {r}')
