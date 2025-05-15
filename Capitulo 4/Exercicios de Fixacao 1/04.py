# Escreva um algoritmo que leia um vetor de 10 posições com
# valores inteiros, aceitando apenas números entre 1 e 5 (inclusive).
# Depois, utilize um outro vetor de cinco posições para calcular a
# distribuição de frequência das ocorrências dos valores possíveis
# para o vetor fornecido. Ou seja, o segundo vetor será um vetor de
# contadores, ele armazenará em sua posição 1 a quantidade de valores
# 1 do vetor original, na posição 2 a quantidade de valores 2 e
# assim por diante. Mostre então esta distribuição calculada.

from clean import limpaTerminal
limpaTerminal()

listaValores = [0] * 10
listaFrequencia = [0] * 5
j = 0

print('=== Digite números de 1 a 5 ===\n')

for i in range(10):
    listaValores[i] = int(input('Número: '))

    match(listaValores[i]):
        case 1:
            listaFrequencia[0] += 1
        case 2:
            listaFrequencia[1] += 1
        case 3:
            listaFrequencia[2] += 1
        case 4:
            listaFrequencia[3] += 1
        case 5:
            listaFrequencia[4] += 1
        case _:
            print('Valor inválido!')

print(f'\n{listaFrequencia}')