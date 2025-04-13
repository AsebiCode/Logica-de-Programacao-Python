# A partir da idade informada de uma pessoa, elabore um algoritmo 
# que informe a classe eleitoral, sabendo que menores de 16 não votam 
# (não votante), que o voto é co gatório para adultos entre 18 e 65 anos 
# (eleitor obrigatório) e que o voto é opcional pas eleitores entre 
# 16 e 18, ou maiores de 65 anos (eleitor facultativo).

from clean import limpaTerminal
limpaTerminal()

print('======= CLASSE ELEITORAL =======\n')
idade = int(input('Informe a sua idade: '))

if idade > 65:
    print('\nVocê é eleitor facultativo.')
elif idade >= 18 and idade <= 65:
    print('\nVocê é eleitor obrigatório.')
elif idade >= 16 and idade < 18:
    print('\nVocê é eleitor opcional.')
else:
    print('\nVocê ainda não pode votar.')