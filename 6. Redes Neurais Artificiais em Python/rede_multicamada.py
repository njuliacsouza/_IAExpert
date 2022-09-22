"""
IAExpert Academy - Redes Neurais Artificiais em Python

September, 2022

Maria Júlia Cristofoletti de Souza
"""

# feedforward

import pandas as pd
import numpy as np
from NeuralNetwork import camada_ocultaI, sigmoid_function, soma, erro, derivada_sigmoide, delta_saida, delta_oculta, ajuste_peso1, ajuste_peso0
import matplotlib.pyplot as plt

###### VARIAVEIS ########
lista_x1 = [0, 0, 1, 1]
lista_x2 = [0, 1, 0, 1]
entradas_xy = list(zip(lista_x1, lista_x2))

# operador XOR esperado
esperados_xor = [0,1,1,0]

# camada de entrada para camada oculta
pesos0_original = [[-0.424, -0.740, -0.961], 
          [0.358, -0.577, -0.469]]
# camada oculta para camada de saída
pesos1_original = [-0.017, -0.893, 0.148]

pesos0 = pesos0_original.copy()
pesos1 = pesos1_original.copy()


###### MODELAGEM ########
epochs = 40000
list_erros = []
for _ in range(epochs):
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
    
    pesos1 = ajuste_peso1(peso_oculta, delta1, pesos1)
    pesos0 = ajuste_peso0(entradas_xy, delta0, pesos0)
    
    

###### RESULTADOS ########
# tabela verdade
OP = pd.DataFrame({
    'x1':lista_x1, 
    'x2':lista_x2, 
    'classe_XOR':esperados_xor,
    'soma': soma_oculta,
    'ativacao': resultado_ativacao,
    'erro': erros
    })

print(OP)
print('Erro médio:', media_erro)
print('Pesos camada oculta:', pesos0)
print('Pesos camada de saída',pesos1)

plt.scatter(y=list_erros, x=[i for i in range(epochs)], s=0.1)
