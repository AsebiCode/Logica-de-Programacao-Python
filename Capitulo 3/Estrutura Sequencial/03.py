# Prepare um algoritmo capaz de inverter um número de três dígitos fornecido,
# ou seja, apresentar primeiro a unidade e, depois, a dezena e a centena.

from clean import limpaTerminal
from math import trunc
limpaTerminal()

num = int(input('Digite um número de 3 dígitos: '))

# Teste: 365
if num < 100 or num > 999:
    print('\nPrecisa ser maior que 100 e menor que 999.')
else:
    centena = trunc(num / 100)
    centena *= 100

    dezena = num - centena
    dezena = trunc(dezena / 10)
    dezena *= 10
    
    unidade = num - (centena + dezena)
    
    print(f'\nUnidade: {unidade}\nDezena: {dezena}\nCentena: {centena}')