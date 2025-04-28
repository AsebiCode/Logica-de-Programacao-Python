# A conversão de graus Fahrenheit para centígrados é obtida pela
# fórmula C - 5/9(F - 32). Escreva um algoritmo que calcule e escreva
# uma tabela de graus centígrados em função de graus Fahrenheit
# que variem de 50 a 150 de 1 em 1.

from clean import limpaTerminal
limpaTerminal()

def Celsius(f):
    return 5/9 * (f - 32)

print('='*33)
print('= ---- TABELA DE CONVERSÃO ---- =')
print('= -- FAHRENHEIT PARA CELCIUS -- =')
print('='*33)

for i in range(50, 151, 1):
    if i >= 100:
        print(f'=   {i}ºF      |      {Celsius(i):.2f}ºC   =')
    else:
        print(f'=   {i}ºF       |      {Celsius(i):.2f}ºC   =')

# O condicional serve para apenas para alinhar a tabela