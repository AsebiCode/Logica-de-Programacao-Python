# Anacleto tem 1,50 metro e cresce dois centímetros por ano;
# Felisberto tem 1,10 metro e cresce três centímetros por ano.
# Construa um algoritmo que calcule e imprima quantos anos
# serão necessários para que Felisberto seja maior que Anacleto.

from clean import limpaTerminal
limpaTerminal()

A, F, anos = 150, 110, 0

while F < A:
    A += 2
    F += 3
    anos += 1

print(f'É necessário {anos} anos para Felisberto supere Anacleto.')