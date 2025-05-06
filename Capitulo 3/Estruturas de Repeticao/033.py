# Realizou-se uma pesquisa para determinar alguns dados estatísticos
# em relação ao conjunto de crianças nascidas em um certo período
# de uma determinada maternidade. Construa um algoritmo que leia o
# número de crianças nascidas nesse período e, depois, em um número
# indeterminado de vezes, o sexo de um recém-nascido prematuro
# ('M' - masculino ou 'F' - feminino) e o número de dias que este
# foi mantido na incubadora.

# Como finalizador, teremos a letra 'X' no lugar do sexo da criança.
# Determine e imprima:
# - a porcentagem de recém-nascidos prematuros;
# - a porcentagem de recém-nascidos meninos e meninas do total de prematuros;
# - a média de dias de permanência dos recém-nascidos prematuros na incubadora;
# - o maior número de dias que um recém-nascido prematuro permaneceu na incubadora.

from clean import limpaTerminal
limpaTerminal()

totalNascimentos = int(input("Número total de crianças nascidas: "))

totalPrematuros, meninos, meninas, diasTotais, maiorTempo = 0, 0, 0, 0, 0

while True:
    sexo = input("\nSexo da criança prematura (M/F): ")
    if sexo == 'X':
        break

    if sexo not in ['mM', 'fF']:
        print("Sexo inválido.")
        continue

    dias = int(input("Dias na incubadora: "))
    totalPrematuros += 1
    diasTotais += dias
    if dias > maiorTempo:
        maiorTempo = dias

    if sexo in 'mM':
        meninos += 1
    else:
        meninas += 1

if totalPrematuros > 0:
    print(f"\n% de prematuros: {(totalPrematuros * 100) / totalNascimentos:.2f}%")
    print(f"% de meninos prematuros: {(meninos * 100) / totalPrematuros:.2f}%")
    print(f"% de meninas prematuras: {(meninas * 100) / totalPrematuros:.2f}%")
    print(f"Média de dias na incubadora: {diasTotais / totalPrematuros:.2f}")
    print(f"Maior tempo na incubadora: {maiorTempo} dias")
else:
    print("\nNenhum prematuro foi registrado.")
