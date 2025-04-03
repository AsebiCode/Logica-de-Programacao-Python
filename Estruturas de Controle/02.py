# 2.2 Escreva um algoritmo que leia três valores inteiros e diferentes
# e mostre-os em ordem decrescente. Utilize para tal uma seleção encadeada.

import clean
clean.limpaTerminal()

print('==== VALORES EM ORDEM DECRESCENTE ====\n')

A = float(input('Digite o valor A: '))
B = float(input('Digite o valor B: '))
C = float(input('Digite o valor C: '))

print('\n======================================\n')

if A < B and A < C:
    if B < C:
        print(f'A < B < C\n{A} < {B} < {C}')
    else:
        print(f'A < C < B\n{A} < {C} < {B}')
elif B < A and B < C:
    if A < C:
        print(f'B < A < C\n{B} < {A} < {C}')
    else:
        print(f'B < C < A\n{B} < {C} < {A}')
elif C < A and C < B:
    if A < B:
        print(f'C < A < B\n{C} < {A} < {B}')
    else: 
        print(f'C < B < A\n{C} < {B} < {A}')
else:
    print('Insira outros valores!')