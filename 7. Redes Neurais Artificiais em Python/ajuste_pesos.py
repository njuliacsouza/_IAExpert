"""
IAExpert Academy - Redes Neurais Artificiais em Python

May, 2022

Maria Júlia Cristofoletti de Souza
"""

import pandas as pd
from NeuralNetwork import ajuste_pesosI

lista_x = [0, 0, 1, 1]
lista_y = [0, 1, 0, 1]
entradas_xy = [[lista_x[i],lista_y[i]] for i in range(len(lista_x))]

# operador E, OU, esperado
esperados_e = [(lista_x[i] & lista_y[i]) for i in range(len(lista_x))]
esperados_ou = [(lista_x[i] | lista_y[i]) for i in range(len(lista_x))]
#esperados_xor = [0,1,1,0]

# tabela verdade
OP_E = pd.DataFrame({
    'x1':lista_x, 
    'x2':lista_y, 
    'classe_E':esperados_e,
    'classe_OU':esperados_ou})

print(OP_E)

# ajuste dos pesos  
pesos_e, i_e = ajuste_pesosI(entradas_xy, esperados_e,)
pesos_ou, i_ou = ajuste_pesosI(entradas_xy, esperados_ou,)
#pesos_xor, i_xor = ajuste_pesosI(entradas_xy, esperados_short, 0.1)
    
print('Pesos operador E:',[round(i, 4) for i in pesos_e])
print('Iterações E:',i_e)
print('Pesos operador OU:',[round(i, 4) for i in pesos_ou])
print('Iterações OU:',i_ou)
#print('Pesos operador XOR:',[round(i, 4) for i in pesos_short])
#print('Iterações XOR:',i_short)

'''
operador SHORT não é linearmente seprável (erro não chega a ZERO), para resolvê-lo,
é preciso implementar uma rede MULTICAMADA
'''