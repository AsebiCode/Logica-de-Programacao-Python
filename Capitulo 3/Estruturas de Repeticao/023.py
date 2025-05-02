# Elabore um algoritmo que imprima todos os números primos
# existentes entre N1 e N2, em que N1 e N2 são números naturais
# fornecidos pelo usuário.

from clean import limpaTerminal
from math import sqrt
limpaTerminal()

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Deve ser > 0
# Calcular sqrt
# Verificar divisões - dividir o número por todos os num naturais menores que a sqrt
# Se resto != 0, num = primo, senão num = não primo

if n1 <= 0 or n2 <= 0:
    print('\nDeve ser maior que 0!')
else:
    for i in range(n1, n2+1):
        if i == 1:
            continue
        primo = True
        raiz = int(sqrt(i))

        for j in range(2, raiz+1):
            if i % j == 0:
                primo = False
                break

        if primo == True:
            print(f'{i} é primo!')