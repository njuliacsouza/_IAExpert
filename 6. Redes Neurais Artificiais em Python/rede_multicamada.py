"""
IAExpert Academy - Redes Neurais Artificiais em Python

September, 2022

Maria Júlia Cristofoletti de Souza
"""

# feedforward

import pandas as pd
import numpy as np
from NeuralNetwork import camada_ocultaI, sigmoid_function, soma, erro

###### VARIAVEIS ########
epocas=100

lista_x1 = [0, 0, 1, 1]
lista_x2 = [0, 1, 0, 1]
entradas_xy = [[lista_x1[i],lista_x2[i]] for i in range(len(lista_x1))]

# operador XOR esperado
esperados_xor = [0,1,1,0]

# camada de entrada para camada oculta
pesos0 = [[-0.424, -0.740, -0.961], 
          [0.358, -0.577, -0.469]]
# camada oculta para camada de saída
pesos1 = [-0.017, -0.893, 0.148]

print(pesos0)
print(pesos1)


###### MODELAGEM ########
# primeira iteracao
peso_oculta = camada_ocultaI(epocas, entradas_xy, pesos0, pesos1)
soma_oculta = [soma(peso_oculta[i], pesos1) for i in range(len(peso_oculta))]
resultado_ativacao = [sigmoid_function(soma_oculta[i]) for i in range(len(soma_oculta))]
# calculo do erro
erros = erro(resultado_ativacao, esperados_xor)
media_erro = np.mean(np.absolute(erros))
# ajuste dos pesos
pesos0_final = pesos0.copy()
pesos1_final = pesos1.copy()


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
print(pesos0_final)
print(pesos1_final)
