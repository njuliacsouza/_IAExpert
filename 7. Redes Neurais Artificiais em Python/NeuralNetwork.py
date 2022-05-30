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

# ajuste dos pesos
def ajuste_pesos(lista_x, lista_y, esperados): 
    pesos = [0, 0]
    erros = [1 for _ in range(len(lista_x))]
    it = 0
    erro_total = 1
    
    while erro_total != 0:  # erro máximo
        erro_total = 0
        it += 1
        for i in range(len(lista_x)):
            resultado = step_function(soma([lista_x[i], lista_y[i]], pesos))
            erro = abs(esperados[i] - resultado)
            erros[i] = erro
            erro_total += erro
            
            pesos[0] = pesos[0] + (taxa_aprendizado * lista_x[i]*erro)
            pesos[1] = pesos[1] + (taxa_aprendizado * lista_y[i]*erro)
    return pesos, it

# aula
def calcula_saida(registro, pesos):
    s = registro.dot(pesos)
    return step_function(s)
    