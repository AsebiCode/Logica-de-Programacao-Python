# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# para homens: ( 72,7 * h)-58;
# para mulheres: ( 62,1 * h)-44,7.

import clean
clean.limpaTerminal()

print('========= PESO IDEAL =========\n')

altura = float(input('Digite a sua altura em metros: '))
sexo = input('Digite o seu sexo (F - feminimo, M - Masculino): ')

match(sexo):
    case sexo if sexo in 'fF':
        pesoIdeal = (62.1 * altura) - 44.7
        print(f'\nPeso ideal: {pesoIdeal:.2f}.')
    case sexo if sexo in 'mM':
        pesoIdeal = (72.7 * altura) - 58
        print(f'\nPeso ideal: {pesoIdeal:.2f}.')
    case _:
        print('Sexo inválido! Digite novamente!')