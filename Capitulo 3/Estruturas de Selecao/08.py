# Elabore um algoritmo que, a partir de um dia, mês e ano fornecidos,
# valide se eles compõem uma data valida. Não deixe de considerar os meses
# com 30 ou 31 dias, e o tratamento de ano bissexto.

from clean import limpaTerminal
limpaTerminal()

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

listaMes30 = (4, 6, 9, 11)
listaMes31 = [1, 3, 5, 7, 8, 10, 12]

if dia < 1 or mes > 12 or mes < 1:
    print('Inválido!')
else: 
    if mes in listaMes31:
        valido = dia <= 31
    elif mes in listaMes30:
        valido = dia <= 30
    elif mes == 2:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        if bissexto:
            valido = dia <= 29
        else:
            valido = dia <= 28
    
    if valido:
        print('Válido!')
    else:
        print('Inválido!')