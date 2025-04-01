# 2.6 Escreva um algoritmo que leia o código de um determinado produto e mostre a sua classificação.
# 1 - Alimento não perecível
# 2, 3 ou 4 - Alimento perecivel
# 5 ou 6 - Vestuário
# 7 - Higiene pessoal
# 8 até 15 - Limpeza e utensílios domésticos
# Qualquer outro código - Inválido

import clean
clean.limpaTerminal()

codigo = int(input('Digite o código do produto: '))

match(codigo):
    case 1:
        print('\nAlimento não perecível')
    case codigo if codigo in range(2, 5):
        print('\nAlimento perecível')
    case 5 | 6:
        print('\nVestuário')
    case 7:
        print('\nHigiene pessoal')
    case codigo if codigo in range(8, 16):
        print('\nLimpeza e utensílios domésticos')
    case _:
        print('\nInválido')