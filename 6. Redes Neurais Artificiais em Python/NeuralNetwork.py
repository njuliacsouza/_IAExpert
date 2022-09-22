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

def ajuste_peso1(oculta, delta, pesos,taxa_aprendizado=0.3, momento=1): # camada oculta
    # (entrada * delta) = lista
    lista = []
    for i in range(len(oculta[0])):    
        soma = 0
        for j in range(len(oculta)):
            soma += oculta[j][i] * delta[j]
        lista.append(soma)
    # peso (n-1) = (peso(n) * momento) + (entrada * delta * taxa de aprendizagem)
    novos_pesos = []
    for i in range(len(pesos)):
        novo_peso = (pesos[i]*momento) + (lista[i]*taxa_aprendizado)
        novos_pesos.append(novo_peso)
    return novos_pesos
        
def ajuste_peso0(entradas, delta, pesos, taxa_aprendizado=0.3, momento=1): # camada entrada
    # entrada * delta
    lista = []
    for neuronio in range(len(delta[0])):
        lista_i = []
        for i in range(len(entradas[0])):
            soma = 0
            for j in range(len(entradas)):
                soma += entradas[j][i] * delta[j][neuronio]
            lista_i.append(soma)
        lista.append(lista_i)
        
    # novos pesos
    novos_pesos = []
    for i in range(len(pesos[0])):
        lista_i = []
        for j in range(len(pesos)):
            novo_peso = (pesos[j][i]* momento) + (lista[i][j]*taxa_aprendizado)
            lista_i.append(novo_peso)
        novos_pesos.append(lista_i)
    
    lista = []
    for i in range(len(novos_pesos[0])):
        lista_i = []
        for j in range(len(novos_pesos)):
            lista_i.append(novos_pesos[j][i])
        lista.append(lista_i)
    novos_pesos = lista.copy()
    
    return novos_pesos
        
        
        
        
        
        
        
        
    