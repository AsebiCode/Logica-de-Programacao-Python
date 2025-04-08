# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
# escreva um algoritmo para gerar o número H. 
# O número N é fornecido pelo usuário.

from clean import limpaTerminal
limpaTerminal()

N = int(input('Até que número você deseja dividir? (1/N)\n'))
H = 1

for i in range(2, N + 1):
    H += 1/i

print(f'\nResultado da divisão 1 + 1/2 + 1/3 + 1/4 + ... + 1/N : {H:.2f}.')