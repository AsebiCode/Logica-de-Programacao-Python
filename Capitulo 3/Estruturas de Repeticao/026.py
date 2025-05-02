# Elabore um algoritmo que determine o valor de S, em que: 
# S = 1/1 - 2/4 + 3/9 - 4/16 + 5/25 - 6/36 ... - 10/100.

from clean import limpaTerminal
limpaTerminal()

S = ''
sinal = ''
j = 1
somaJ = 3

for i in range(1, 11):
    sinal = '-' if i % 2 == 0 else '+'

    termo = f'{i}/{j}'
    # Evita o último sinal para não dar erro de sintaxe
    if i == 1:
        S += termo
    else:
        S += f' {sinal} {termo}'
    
    j += somaJ
    somaJ += 2

result = eval(S)
print(f'\nS = {S}')
print(f'S = {result}')