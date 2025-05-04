# Calcule o imposto de renda de um grupo de dez contribuintes,
# considerando que os dados de cada contribuinte, número do CPF,
# número de dependentes e renda mensão são valores fornecidos
# pelo usuário. Para cada contribuinte será feito um desconto
# de 5% do salário mínimo por dependente.

# Os valores da alíquota para cálculo do imposto são:
# - Até 2 salários mínimos = isento
# - 2 a 3 salários mínimos = 5%
# - 3 a 5 salários mínimos = 10%
# - 5 a 7 salários mínimos = 15%
# - acima de 7 salários mínimos = 20%

# Observe que deve ser fornecido o valor atual do salário mínimo
# para que o algoritmo calcule os valores corretamente.

from clean import limpaTerminal
limpaTerminal()

salarioMinimo = float(input('Informe o valor do salário mínimo atual: R$'))

for i in range(10):
    print(f'\n== {i+1}º Contribuinte ==')
    cpf = input('CPF: ')
    numDependentes = int(input('Número de dependentes: '))
    rendaMensal = float(input('Renda mensal: R$'))

    desconto = 0.05 * salarioMinimo * numDependentes
    rendaCorrigida = rendaMensal - desconto

    if rendaCorrigida <= (salarioMinimo * 2):
        print('\nIsento')
    elif rendaCorrigida > (salarioMinimo * 2) and rendaCorrigida <= (salarioMinimo * 3):
        aliquota = rendaCorrigida * 0.05
        print(f'\nAlíquota: R${aliquota:.2f}')
    elif rendaCorrigida > (salarioMinimo * 3) and rendaCorrigida <= (salarioMinimo * 5):
        aliquota = rendaCorrigida * 0.1
        print(f'\nAlíquota: R${aliquota:.2f}')
    elif rendaCorrigida > (salarioMinimo * 5) and rendaCorrigida <= (salarioMinimo * 7):
        aliquota = rendaCorrigida * 0.15
        print(f'\nAlíquota: R${aliquota:.2f}')
    else:
        aliquota = rendaCorrigida * 20
        print(f'\nAlíquota: R${aliquota:.2f}')