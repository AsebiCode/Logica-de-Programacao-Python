# Esrava um algoritmo que imprima todas as possibilidades
# de que no lançamento de dois dados tenhamos o valor 7
# como resultado da soma dos valores de cada dado

from clean import limpaTerminal
limpaTerminal()

print('Possibilidades dos Dados\n')
j = 7
for i in range(1, 7):
    print(f'Dado 1 ({i}) + Dado 2 ({j-1}) = 7')
    j -= 1