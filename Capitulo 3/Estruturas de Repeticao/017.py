# Construa um algoritmo que gere os 20 primeiros termos
# de uma série tal qual a de Fibonacci, mas que cujos
# dois primeiros termos sejam fornecidos pelo usuário.

from clean import limpaTerminal
limpaTerminal()

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Dois primeiros termos
print(f'\n{n1}\n{n2}')

fibonacci = 0
acm = n1 + n2

for i in range(18):
    prox = n1 + n2
    print(prox)
    n1 = n2
    n2 = prox