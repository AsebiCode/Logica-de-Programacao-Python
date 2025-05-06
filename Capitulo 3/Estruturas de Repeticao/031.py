# Foi realizada uma pesquisa sobre algumas características
# físicas da população de uma certa região, a qual coletou
# os seguintes dados referentes a cada habitante para análise:
# - sexo ('M' - masculino ou 'F' - feminino);
# - cor dos olhos ('A' - azuis, 'V' - verdes ou 'C' - castanho);
# - cor dos cabelos ('L' - loiros, 'C' - castanhos ou 'P' - pretos);
# - idade.

# Faça um algoritmo que determine e escreva:
# - a maior idade dos habitantes;
# - a porcentagem entre os indivíduos do sexo masculino,
# cuja idade está entre 18 e 35 anos, inclusive;
# - a porcentagem do total de indivíduos do sexo feminino
# cuja idade está entre 18 e 35 anos, inclusive, e que
# tenham olhos verdes e cabelos loiros.

# O final do conjunto de habitantes é reconhecido pelo valor -1 entrando como idade.

from clean import limpaTerminal
limpaTerminal()

totalPessoas, maiorIdade, totalM, totalF, totalLoiras, totalHomens = 0, 0, 0, 0, 0, 0

while True:
    sexo = input('\nSexo:\nM - Masculino ou F - Feminino: ')
    corOlho = input('Cor dos Olhos:\nA - Azuis, V - Verdes ou C - Castanho: ')
    corCabelo = input('Cor do Cabelo:\nL - Loiros, C - Castanhos ou P - Pretos: ')
    idade = int(input('Idade:'))

    if idade == -1:
        break

    # Maior idade
    if idade > maiorIdade:
        maiorIdade = idade

    # Masculino
    if sexo in 'mM':
        totalHomens += 1
        if idade >= 18 and idade <= 35:
            totalM += 1

    # Feminino
    elif sexo in 'fF':
        if idade >= 18 and idade <= 35:
            totalF += 1
            # Olho verde e Cabelo loiro
            if corOlho in 'vV' and corCabelo in 'lL':
                totalLoiras += 1

    else:
        print("\nSexo Inválido!")
        continue

    totalPessoas += 1
    
porcentagemM = (totalM * 100) / totalHomens if totalHomens else 0
porcentagemF = (totalLoiras * 100) / totalF if totalF else 0

print(f"\nMaior idade: {maiorIdade}")
print(f'Homens entre 18 a 35 anos: {porcentagemM:.2f}%')
print(f'Mulheres entre 18 a 35 anos, olhos verdes e loiras: {porcentagemF:.2f}%')