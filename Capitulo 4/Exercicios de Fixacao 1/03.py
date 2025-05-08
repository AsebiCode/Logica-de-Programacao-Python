# Crie um algoritmo que leia um vetor de 10 posições inteiras.
# Depois, solicite para o usuário um número que ele gostaria de
# pesquisar neste vetor, caso o número exista no vetor, mostre
# em qual(is) posição(ões) ele foi encontrado e quantas
# ocorrências foram detectadas.

from clean import limpaTerminal
limpaTerminal()

listaNumeros = [0] * 10
posicoes = []

for i in range(10):
    listaNumeros[i] = int(input('Número: '))

pesquisa = int(input('\nQue número deseja buscar?\n'))

for i in range(10):
    if pesquisa == listaNumeros[i]:
        posicoes.append(i)

print(f'\nLista: {listaNumeros}\nPosições: {posicoes}')