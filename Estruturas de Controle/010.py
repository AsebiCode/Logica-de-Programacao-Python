# O IMC-Indice de Massa Corporal - é um critério da Organização Mundial de Saúde para indicar a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição.
# abaixo de 18,5 - abaixo do peso
# entre 18,5 e 25 - peso normal
# entre 25 e 30 - acima do peso
# acima de 30 - obeso

import clean
clean.limpaTerminal()
from math import pow

print('======= ÍNDICE DE MASSA CORPORAL =======\n')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (pow(altura, 2))

match(imc):
    case imc if imc < 18.5:
        print(f'\nAbaixo do peso! Seu IMC: {imc:.2f}')
    case imc if imc >= 18.5 and imc < 25:
        print(f'\nPeso normal! Seu IMC: {imc:.2f}')
    case imc if imc >= 25 and imc < 30:
        print(f'\nAcima do peso! Seu IMC: {imc:.2f}')
    case imc if imc >= 30:
        print(f'\nObeso! Seu IMC: {imc:.2f}')
    case _:
        print('Algum valor está errado! Digite novamente!')