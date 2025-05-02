# Construa um algoritmo que leia um conjunto de dados
# contendo altura e sexo ('M' para masculino e 'F' para
# feminino) de 50 pessoas e, depois, calcule e escreva:
# - a maior e a menor altura do grupo;
# - a média de altura das mulheres;
# - o número de homens e a diferença porcentual
# entre eles e as mulheres.

from clean import limpaTerminal
limpaTerminal()

maiorAltura, menorAltura, alturaF, numF, numH, totalPessoas = 0, 300, 0, 0, 0, 0

for i in range(5):
    print(f'\n{i+1}º Pessoa')
    sexo = input('Sexo (M/F): ')

    if sexo not in 'mMfF':
        print('Sexo inválido!')
        break

    altura = int(input('Altura em cm: '))

    if altura > maiorAltura:
        maiorAltura = altura
    if altura < menorAltura:
        menorAltura = altura

    if sexo in 'mM':
        numH += 1
    else:
        alturaF += altura
        numF += 1
    
    totalPessoas += 1

mediaAlturaF = alturaF / numF if numF > 0 else 0
difPorcent = abs(numH - numF) * 100 / totalPessoas

print(f'\nMAIOR ALTURA: {maiorAltura} cm\nMENOR ALTURA: {menorAltura} cm')
print(f'MÉDIA ALTURA MULHERES: {mediaAlturaF:.2f} cm')
print(f'DIFERENÇA % ENTRE SEXOS: {difPorcent:.1f}%')