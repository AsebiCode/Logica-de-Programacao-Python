# 2.3 Desenvolva um algoritmo que calcule as raízes 
# de uma equação do 2º grau, na forma A* x ^ 2 + Bx + C 
# levando em consideração a existência de raízes reais.

import clean, math
clean.limpaTerminal()

print("======== EQUAÇÃO DE SEGUNDO GRAU ========\n")

coeficienteA = float(input('Digite o valor do coeficiente A: '))
coeficienteB = float(input('Digite o valor do coeficiente B : '))
coeficienteC = float(input('Digite o valor do coeficiente C: '))

print('\n=========================================\n')
print(f'Equação: {coeficienteA}x² + {coeficienteB}x + {coeficienteC} = 0')

delta = (coeficienteB ** 2) - (4 * coeficienteA * coeficienteC)
print(f'Δ = {delta}')

if delta < 0:
    print('A equação não possui raizes reais!')
    print('\n=========================================')
else:
    raizDelta = math.sqrt(delta)
    x1 = (-coeficienteB + raizDelta) / (2 * coeficienteA)
    x2 = (-coeficienteB - raizDelta) / (2 * coeficienteA)

    print('\n=========================================')
    print('\nRESULTADOS:')

    print(f'\nx1: {x1:.2f}')
    print(f'x2: {x2:.2f}')