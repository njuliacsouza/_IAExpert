"""
IAExpert Academy - Redes Neurais Artificiais em Python

September, 2022

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
    return 1/(1+np.exp(-soma))

# camada entrada: 0
# camada oculta: 1
# camada saida: 2
def camada_ocultaI(entrada, peso0, peso1):
    entrada = np.array(entrada)
    peso0 = np.array(peso0)
    peso1 = np.array([[i] for i in peso1])
    
    sinapse_0 = np.dot(entrada, peso0)
    camada_1 = sigmoid_function(sinapse_0)
    
    return camada_1, sinapse_0

def erro(calculado, correta):
    return [correta[i] - calculado[i] for i in range(len(correta))]

def derivada_sigmoide(x):  
    return x * (1-x)

def delta_saida(erros, derivadas):
    return [erros[i]*derivadas[i] for i in range(len(erros))]

def delta_oculta(derivadas, pesos, delta_saida):
    resultado = []
    for i in range(len(derivadas)):
        res_i = []
        for j in range(len(derivadas[0])):
            res_i.append(pesos[j] * derivadas[i][j] * delta_saida[i])
        resultado.append(res_i)
    return resultado

def ajuste_peso1(oculta, delta, taxa_aprendizado=0.01, momento=1):
    # (entrada * delta)
    lista = []
    for i in range(len(oculta[0])):    
        soma = 0
        for j in range(len(oculta)):
            soma += oculta[j][i] * delta[j]
        lista.append(soma)
    # peso (n-1) = (peso(n) * momento) + (entrada * delta * taxa de aprendizagem)
    return lista
        
        
        
        
        
        
        
        
        
        
    