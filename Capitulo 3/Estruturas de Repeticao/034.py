# Um cinema possui capacidade de 100 lugares e está sempre
# com ocupação total. Certo dia, cada espectador respondeu
# a um questionário, no qual constava:
# - sua idade;
# - sua opinião em relação ao filme, segundo as seguintes notas:
#   - A = Ótimo
#   - B = Bom
#   - C = Regular
#   - D = Ruim
#   - E = Péssimo

# Elabore um algoritmo que, lendo esses dados, calcule e imprima:
# - a quantidade de respostas "ótimo";
# - a diferença porcentual entre respostas "bom" e "regular";
# - a média de idade das pessoas que responderam "ruim";
# - a porcentagem de respostas "péssimo" e a maior idade que utilizou essa opção;
# - a diferença de idade entre a maior idade que respondeu "ótimo" e
# a maior idade que respondeu "ruim".

from clean import limpaTerminal
limpaTerminal()

qtddA, qtddB, qtddC, qtddD, qtddE = 0, 0, 0, 0, 0
maiorIdadeA, maiorIdadeD, somaIdadesD, maiorIdadeE = 0, 0, 0, 0
totalNotas = 100

for i in range(totalNotas):
    print(f"\n{i+1}º Espectador")
    idade = int(input('Idade: '))

    print('[A] - Ótimo\n[B] = Bom\n[C] - Regular\n[D] - Ruim\n[E] - Péssimo')
    nota = input('Nota: ')

    match(nota):
        case nota if nota in 'aA':
            qtddA += 1
            if idade > maiorIdadeA:
                maiorIdadeA = idade

        case nota if nota in 'bB':
            qtddB += 1

        case nota if nota in 'cC':
            qtddC += 1

        case nota if nota in 'dD':
            qtddD += 1
            somaIdadesD += idade
            if idade > maiorIdadeD:
                maiorIdadeD = idade

        case nota if nota in 'eE':
            qtddE += 1
            if idade > maiorIdadeE:
                maiorIdadeE = idade

        case _:
            print('Nota inválida!')
            continue

diffPorcentual = qtddB - qtddC
mediaIdadeD = somaIdadesD / qtddD if qtddD > 0 else 0
diffIdade = maiorIdadeA - maiorIdadeE

print(f'\n[A] - Ótimo - {qtddA}%')
print(f'\n[B] - Bom - {qtddB}%')
print(f'\n[C] - Regular - {qtddC}%')
print(f'\n[D] - Ruim - {qtddD}%')
print(f'\n[E] - Péssimo - {qtddE}%')

print(f'Diferença porcentual entre B e C: {diffPorcentual}%')
print(f'Média de idade das pessoas que responderam D: {mediaIdadeD}')
print(f'Maior idade que respondeu E: {maiorIdadeE}')
print(f'Diferença das maiores idade que responderam A e E: {diffIdade}')