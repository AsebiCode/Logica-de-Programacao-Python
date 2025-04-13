# Construa um algoritmo capaz de dar a classificação olímpica
# de três paises informada. Para cada país é informado o nome e a
# quantidade de medalhas de ouro, prata e bronze. Considere que cada
# medalha de ouro tem peso 3, cada prata tem peso 2 e cada bronas peso 1.

from clean import limpaTerminal
limpaTerminal()

pais1 = input('Digite o nome do primeiro país: ')
ouro = int(input('Quantidade de medalhas de ouro: '))
prata = int(input('Quantidade de medalhas de prata: '))
bronze = int(input('Quantidade de medalhas de bronze: '))
peso1 = (ouro*3) + (prata*2) + (bronze)

pais2 = input('\nDigite o nome do segundo país: ')
ouro = int(input('Quantidade de medalhas de ouro: '))
prata = int(input('Quantidade de medalhas de prata: '))
bronze = int(input('Quantidade de medalhas de bronze: '))
peso2 = (ouro*3) + (prata*2) + (bronze)

pais3 = input('\nDigite o nome do terceiro país: ')
ouro = int(input('Quantidade de medalhas de ouro: '))
prata = int(input('Quantidade de medalhas de prata: '))
bronze = int(input('Quantidade de medalhas de bronze: '))

peso3 = (ouro*3) + (prata*2) + (bronze)

print('\n======== PÓDIO ========')

if peso1 > peso2 and peso1 > peso3:
    if peso2 > peso3:
        print(f'\n1º {pais1} - {peso1}\n2º {pais2} - {peso2}\n3º {pais3} - {peso3}')
    else:
        print(f'\n1º {pais1} - {peso1}\n2º {pais3} - {peso3}\n3º {pais2} - {peso2}')
elif peso2 > peso1 and peso2 > peso3:
    if peso1 > peso3:
        print(f'\n1º {pais2} - {peso2}\n2º {pais1} - {peso1}\n3º {pais3} - {peso3}')
    else:
        print(f'\n1º {pais2} - {peso2}\n2º {pais3} - {peso3}\n3º {pais1} - {peso1}')
elif peso3 > peso1 and peso3 > peso2:
    if peso1 > peso2:
        print(f'\n1º {pais3} - {peso3}\n2º {pais1} - {peso1}\n3º {pais2} - {peso2}')
    else:
        print(f'\n1º {pais3} - {peso3}\n2º {pais2} - {peso2}\n3º {pais1} - {peso1}')