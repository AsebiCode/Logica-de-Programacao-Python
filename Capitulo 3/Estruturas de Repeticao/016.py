# Faça um algoritmo que obtenha o resultado de uma
# exponenciação para qualquer base e expoente inteiro
# fornecidos, sem utilizar a operação de exponenciação (pot).

from clean import limpaTerminal
limpaTerminal()

base = int(input('Digite o valor da base: '))
exp = int(input('Digite o valor do expoente: '))

result = 1
for i in range(1, exp+1):
    result *= base

print(f'\nResultado: {result}')