# Construa um algoritmo que verifique se um número fornecido pelo usuário é primo ou não.

from clean import limpaTerminal
limpaTerminal()

num = float(input('Digite um número: '))

if num % 2 == 0 :
    print(f'\n{num} é par!')
else:
    print(f'\n{num} é ímpar!')