# Escreva um algoritmo que calcule e escreva a soma dos
# dez primeiros termos da seguinte série:
# 2/500 - 5/450 + 2/400 - 5/350 + ...

from clean import limpaTerminal
limpaTerminal()

F, sinal, termo = '', '', ''
numerador, denominador = 0, 500

for i in range(2, 12):
    sinal = '-' if i % 2 == 0 else '+'
    numerador = 2 if i % 2 == 0 else 5

    termo = f'{numerador}/{denominador}'
    if i == 2:
        F += termo
    else:
        F += f' {sinal} {termo}'

    denominador -= 50

print(f'\n{F}')
print(f'RESULTADO: {eval(F)}')