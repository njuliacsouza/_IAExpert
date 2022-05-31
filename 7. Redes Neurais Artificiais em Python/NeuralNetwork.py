"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import numpy as np

taxa_aprendizado = 0.1

def soma(entradas: list, pesos: list) -> float:
    s = 0 # soma
    
    for i in range(len(entradas)):
        s += entradas[i] * pesos[i]
    
    return s

def step_function(soma: float) -> int:
    if (soma >= 1):
       return 1
    return 0

def soma_II(entradas: list, pesos: list) -> float:
    entradas = np.array(entradas)
    pesos = np.array(pesos)
    
    return entradas.dot(pesos)

# ajuste dos pesos - Perceptron de uma camada
def ajuste_pesosI(entradas, esperados): 
    pesos = [0, 0]
    it = 0
    erro_total = 1
    
    while (erro_total != 0):  # erro máximo
        erro_total = 0
        it += 1
        for i in range(len(esperados)):
            resultado = step_function(soma_II(np.asarray(entradas[i]), pesos))
            erro = abs(esperados[i] - resultado)
            erro_total += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizado * entradas[i][j]*erro)
    return pesos, it

def sigmoid_function(soma: float) -> float:
    return round(1/(1+np.exp(-soma)), 5)
    