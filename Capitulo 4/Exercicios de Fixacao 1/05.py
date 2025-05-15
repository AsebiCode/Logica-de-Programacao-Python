# Desenvolva um algoritmo que leia um vetor de 20 posições inteiras
# e o coloque em ordem crescente, utilizando como estratégia de ordenação
# a comparação de pares de elementos adjacentes, permutando-os quando
# estiverem fora de ordem, até que todos estejam ordenados. Este método
# de ordenação clássico é conhecido como Ordenação por Permutação ou
# como Bubblesort (ordenação por bolhas).

from clean import limpaTerminal
limpaTerminal()
from random import randint

arrNum = [randint(1, 100) for i in range(20)]
tamanho = len(arrNum)

print(f'LISTA:\n{arrNum}')

for i in range(tamanho - 1):
    for j in range(tamanho - i - 1):
        if arrNum[j] > arrNum[j+1]:
            arrNum[j], arrNum[j+1] = arrNum[j+1], arrNum[j]

print(f'\nORDENADO:\n{arrNum}')