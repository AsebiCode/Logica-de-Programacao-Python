# Elabore um algoritmo que calcule um número inteiro que mais se
# aproxime da raiz quadrada de um número fornecido pelo usuário.

from clean import limpaTerminal
limpaTerminal()
from math import sqrt, trunc

num = int(input('Digite um número para calcular raiz quadrada: '))
raiz = trunc(sqrt(num))

print(f'\n Resultado aproximado: {raiz}.')