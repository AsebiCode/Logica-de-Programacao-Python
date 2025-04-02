# Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual a operação aritmética escolhida.
# Símbolos: + - * /

import clean, math
clean.limpaTerminal()

print('========= OPERAÇÃO =========\n')

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
operador = input('Digite o operador: ')

if operador != '+' and operador != '-' and operador != '*' and operador != '/':
    print('Operador inválido!')
else:
    calculo = (f'{num1} {operador} {num2}')
    result = eval(calculo)
    print(f'\nRESULTADO: {result:.2f}')