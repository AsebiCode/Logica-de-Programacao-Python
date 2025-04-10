# Um dado comerciante maluco cobra 10% de acréscimo para cada prestação 
# em atraso depois da um desconto de 10% sobre esse valor. 
# Faça um algoritmo que solicite o valor da prestação em atraso e apresente 
# o valor final a pagar, assim como o prejuizo do comerciante na operação.

from clean import limpaTerminal
limpaTerminal()

prestacao = float(input('Digite o valor da prestação atrasada: '))

valorAtraso = prestacao + (prestacao * 0.1)
valorFinal = valorAtraso - (valorAtraso * 0.1)
prejuizo = prestacao - valorFinal

print(f'\nValor final a pagar: R${valorFinal:.2f}\nPrejuízo do comerciante: R${prejuizo:.2f}')