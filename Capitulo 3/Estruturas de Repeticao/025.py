# Prepare um algoritmo que calcule o valor de H,
# sendo que ele é determinado ela série
# H = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

from clean import limpaTerminal
limpaTerminal()

H = 0
j = 1
for i in range(1, 100, 2):
    H += i/j
    j += 1

print(f'H = {H}')