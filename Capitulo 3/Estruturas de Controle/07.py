# Elabore um algoritmo que dada a idade de um nadador 
# classifica-o em uma das seguintes categorias:

# Infantil A -  5 até 7 anos
# Infantil B - 8 até 10 anos
# Juvenil A - 11 até 13 anos
# Juvenil B - 14 até 17 anos
# Adulto - Maiores de 18 anos

from clean import limpaTerminal
limpaTerminal()

print('======= CLASSIFICAÇÃO DE NADADORES =======\n')

idade = int(input('Digite a sua idade: '))

match(idade):
    case 5 | 6 | 7:
        print('\nInfantil A')
    case 8 | 9 | 10:
        print('\nInfantil B')
    case 11 | 12 | 13:
        print('\nJuvenil A')
    case 14 | 15 | 16 | 17:
        print('\nJuvenil B')
    case idade if idade >= 18:
        print('\nAdulto')
    case _:
        print('\nValor inválido!')