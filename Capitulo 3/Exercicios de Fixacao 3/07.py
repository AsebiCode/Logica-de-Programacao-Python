# Escreva um algoritmo que leia um conjunto de 
# 20 números inteiros e mostre o maior e o menor valor fornecidos.

from clean import limpaTerminal
from random import randint # Fornece os 20 números
limpaTerminal()

valores = [randint(1, 100) for i in range(20)]
maiorValor = max(valores)
menorValor = min(valores)

print(valores)
print(f'\nMaior valor: {maiorValor}\nMenor valor: {menorValor}')