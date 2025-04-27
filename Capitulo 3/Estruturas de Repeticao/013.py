# Elabore um algoritmo que obtenha o mínimo múltiplo comum (MMC)
# entre dois números fornecidos.

from clean import limpaTerminal
limpaTerminal()

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

resultado_mmc = (n1 * n2) // mdc(n1, n2)

print(f'\nMMC: {resultado_mmc}')