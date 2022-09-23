"""
IAExpert Academy - Redes Neurais Artificiais em Python

September, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

from NeuralNetwork import camada_ocultaI, sigmoid_function, soma, erro, derivada_sigmoide, delta_saida, delta_oculta, ajuste_peso1, ajuste_peso0

###### VARIAVEIS ########
base = datasets.load_breast_cancer()
entradas_xy = base.data

# operador XOR esperado
esperados_xor = base.target

neuronios = 5
# camada de entrada para camada oculta
pesos0_original = 2*np.random.random((30,neuronios)) - 1
# camada oculta para camada de saída
pesos1_original = 2*np.random.random((neuronios,)) - 1

pesos0 = pesos0_original.copy()
pesos1 = pesos1_original.copy()


###### MODELAGEM ########
epochs = 10000
list_erros = []
for epoch in range(epochs):
    peso_oculta, sinapse0 = camada_ocultaI(entradas_xy, pesos0, pesos1)
    soma_oculta = [soma(peso_oculta[i], pesos1) for i in range(len(peso_oculta))]
    resultado_ativacao = [sigmoid_function(soma_oculta[i]) for i in range(len(soma_oculta))]
    # calculo do erro
    erros = erro(resultado_ativacao, esperados_xor)
    media_erro = np.mean(np.absolute(erros))
    list_erros.append(media_erro)
    # ajuste dos pesos - 1
    derivadas1 = [derivada_sigmoide(resultado_ativacao[i]) for i in range(len(resultado_ativacao))]
    derivadas0 = []
    for i in range(len(sinapse0)):
        lista_i = []
        for j in range(len(sinapse0[0])):
            lista_i.append(derivada_sigmoide(sigmoid_function(sinapse0[i][j])))
        derivadas0.append(lista_i)
        
    delta1 = delta_saida(erros, derivadas1)
    delta0 = delta_oculta(derivadas0, pesos1, delta1)
    pesos1 = ajuste_peso1(peso_oculta, delta1, pesos1, taxa_aprendizado=0.3) 
    pesos0 = ajuste_peso0(entradas_xy, delta0, pesos0, taxa_aprendizado=0.3)
    
    if ((epoch+1)%100 ==0) or (epoch==0):
        print('Epoch:',epoch+1, 'erro médio:', media_erro)
    
    


plt.scatter(y=list_erros, x=[i for i in range(epochs)], s=2) 
plt.title('Erro x  epoch')


