# Construa um algoritmo que calcule a média ponderada entre cinco números
# quaisquer, sendo que os pesos a serem aplicados são 1, 2, 3, 4 e 5 respectivamente.

from clean import limpaTerminal
from random import randint # Oferece 5 números
limpaTerminal()

valores = [randint(1, 10) for i in range(5)]
print(valores)

MP = 0
j = 1

for i in valores:
    MP += i * j
    j += 1

MP = MP / 15
print(f'\nMédia Ponderada: {MP:.1f}')