# Escreva um alqoritmo que, a partir de um mês fornecido (número inteiro de 1 a 12),
#  apresente o nome dele por extenso ou uma mensagem de mês inválido.

from clean import limpaTerminal
limpaTerminal()

print('====== MÊS POR EXTENSO ======\n')
mes = int(input('Digite o número do mês: '))

match(mes):
    case 1:
        print('Janeiro')
    case 2:
        print('Fevereiro')
    case 3:
        print('Março')
    case 4:
        print('Abril')
    case 5:
        print('Maio')
    case 6:
        print('Junho')
    case 7:
        print('Julho')
    case 8:
        print('Agosto')
    case 9:
        print('Setembro')
    case 10:
        print('Outubro')
    case 11:
        print('Novembro')
    case 12:
        print('Dezembro')
    case _:
        print('Inválido!')