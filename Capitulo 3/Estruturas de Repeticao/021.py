# Em uma eleição presidencial, existem quatro candidatos. Os votos
# são informados por código. Os dados utilizados para a escrutinagem
# obedecem à seguinte codificação:
# - 1, 2, 3, 4 = voto para os respectivos candidatos;
# - 5 = voto nulo;
# - 6 = voto em branco.
# Elabore um algoritmo que calcule e escreva:
# - o total de votos para cada candidato e seu porcentual sobre o total;
# - o total de votos nulos e seu porcentual sobre o total;
# - o total de votos em branco e seu porcentual sobre o total.
# Como finalizador do conjunto de votos, tem-se o valor 0.

from clean import limpaTerminal
limpaTerminal()

ca1, ca2, ca3, ca4, branco, nulo = 0, 0, 0, 0, 0, 0

while True:
    print('='*32)
    print('= --- ELEIÇÃO PRESIDENCIAL --- =')
    print('='*32)
    print('= [1] | Candidato 1            =')
    print('= [2] | Candidato 2            =')
    print('= [3] | Candidato 3            =')
    print('= [4] | Candidato 4            =')
    print('= [5] | Nulo                   =')
    print('= [6] | Branco                 =')
    print('= [0] | Sair                   =')
    print('='*32)
    opcao = int(input('Opção: '))

    match(opcao):
        case 1:
            ca1 += 1
        case 2:
            ca2 += 1
        case 3:
            ca3 += 1
        case 4:
            ca4 += 1
        case 5:
            nulo += 1
        case 6:
            branco += 1
        case 0:
            print('\n        FIM DA VOTAÇÃO ')
            break
        case _:
            print('\n        CÓDIGO INVÁLIDO')
            continue

totalVotos = ca1 + ca2 + ca3 + ca4 + branco + nulo

def PorcentagemVotos(votos):
    return (votos * 100) / totalVotos

print('='*32)
print(f'[1] | {ca1} voto(s) - {PorcentagemVotos(ca1):.1f}%')
print(f'[2] | {ca2} voto(s) - {PorcentagemVotos(ca2):.1f}%')
print(f'[3] | {ca3} voto(s) - {PorcentagemVotos(ca3):.1f}%')
print(f'[4] | {ca4} voto(s) - {PorcentagemVotos(ca4):.1f}%')
print(f'[5] | {nulo} voto(s) - {PorcentagemVotos(nulo):.1f}%')
print(f'[6] | {branco} voto(s) - {PorcentagemVotos(branco):.1f}%')
print(f'\nTOTAL DE VOTOS: {totalVotos}')
print('='*32)