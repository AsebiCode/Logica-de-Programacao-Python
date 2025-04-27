# Faça um algoritmo capaz de obter o quociente inteiro da
# divisão de dois números fornecidos, sem utilizar a operação
# de divisão (/) nem divisão inteira (div).

# A solução envolve subtrações sucessivas do dividendo pelo divisor!

from clean import limpaTerminal
limpaTerminal()

n1 = int(input('Informe o dividendo: '))
n2 = int(input('Informe o divisor: '))

quociente = 0
while n1 >= n2:
    n1 -= n2
    quociente += 1

print(f'\nQuociente: {quociente}')