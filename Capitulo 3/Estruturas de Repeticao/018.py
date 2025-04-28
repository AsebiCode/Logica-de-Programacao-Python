# Construa um algoritmo que, dado um conjunto de valores inteiros
# e positivos, determine o menor e o maior valor do conjunto.
# O final do conjunto de valores é conhecido pelo valor -1 que
# não deve ser considerado.

from clean import limpaTerminal
limpaTerminal()

num, maior, menor, ant, i = 0, 0, 0, 0, 0

while num >= 0:
    num = int(input(f'Digite o {i+1}º número do conjunto: '))
    if num != -1:
        maior = num
        menor = num
        i = 1
    else:
        print('Nenhum número válido informado.')

    while num != -1:
        num = int(input(f'Digite o {i+1}º número do conjunto: '))
        if num == -1:
            break
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        i += 1

print(f'\nMAIOR: {maior}\nMENOR: {menor}')