# Elabore um algoritmo que calcule a área de um círculo qualquer de raio fornecido.

from clean import limpaTerminal
from math import pi, pow
limpaTerminal()

raio = float(input('Digite o raio do círculo: '))
Area = pi * pow(raio, 2)

print(f'\nResultado: {Area:.2f}')