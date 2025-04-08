# Elabore um algoritmo que calcule N! (fatorial de N),
# sendo que o valor inteiro de N é fornecido pelo usuário. Sabendo que:
# N! = 1*2*3* ... * (N − 1) * N;
# 0! = 1, por definição.

from clean import limpaTerminal
limpaTerminal()

N = int(input('Digite um número para calcular fatorial: '))
fatorial = 1

if N == 0:
    print('\nResultado do fatorial: 1')
else:
    for i in range(2, N + 1):
        fatorial = fatorial * i

    print(f'\nResultado do fatorial: {fatorial}')