# Construa um algoritmo que calcule o valor dos dez
# primeiros termos da série H, em que:
# H = 1/pot(1,3) - 1/pot(3,3) + 1/pot(5/3) - 1/pot(7/3) + 1/pot(9,3) - ...

from clean import limpaTerminal
from math import pow
limpaTerminal()

H, sinal = '', ''
j = 1

for i in range(1, 11):
    sinal = '-' if i % 2 == 0 else '+'
    
    potencia = pow(j,3)
    termo = f'1/{potencia}'

    if i == 1:
        H += termo
    else:
        H += f' {sinal} {termo}'

    j += 2

print(f'H = {H}')
print(f'RESULTADO: {eval(H)}')