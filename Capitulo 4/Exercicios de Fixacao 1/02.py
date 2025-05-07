# Elabore um algoritmo que efetue a leitura de dois vetores
# de 20 posições de valores inteiros. Depois efetue as respectivas
# operações indicadas por outro vetor de 20 posições de caracteres
# também fornecido pelo usuário, contendo uma das quatro operações
# aritméticas básicas (testando a validade da entrada de dados) e
# armazenando os resultados em um quarto vetor. Mostre todos os
# vetores utilizados.

from clean import limpaTerminal
limpaTerminal()

arrayNum1, arrayNum2, arrayResult = [0] * 20, [0] * 20, [0] * 20
arrayOp = [''] * 20

for i in range(20):
    print(f'\n{i+1}º Operação')
    arrayNum1[i] = float(input('Número 1: '))
    arrayOp[i] = input('Operação: ')
    arrayNum2[i] = float(input('Número 2: '))

    match(arrayOp[i]):
        case '+':
            arrayResult[i] = arrayNum1[i] + arrayNum2[i]
        case '-':
            arrayResult[i] = arrayNum1[i] - arrayNum2[i]
        case '/':
            arrayResult[i] = arrayNum1[i] / arrayNum2[i]
        case '*':
            arrayResult[i] = arrayNum1[i] * arrayNum2[i]
        case _:
            print('Operador inválido!')

print('\n======================')
for i in range(20):
    print(f'{arrayNum1[i]} {arrayOp[i]} {arrayNum2[i]} = {arrayResult[i]}')