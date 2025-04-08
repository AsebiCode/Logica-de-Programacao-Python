# A série de Fibonacci é formada pela seguinte sequência: 
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... etc. Escreva um algoritmo que 
# gere a série de Fibonacci até o vigésimo termo.

from clean import limpaTerminal
limpaTerminal()

fibonacci = 0
acm = 1

for i in range(1,21):
    print(fibonacci + acm)
    ant = fibonacci
    fibonacci = acm
    acm = ant + fibonacci