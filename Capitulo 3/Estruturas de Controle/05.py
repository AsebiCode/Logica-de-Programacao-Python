# 2.5 Faça um algoritmo que leia o ano de nascimento de uma pessoa, 
# calcule e mostre sua idade e, também, verifique e mostre se ela 
# já tem idade para votar (16 anos ou mais) e para 
# conseguir a carteira de habilitação (18 anos ou mais).

from clean import limpaTerminal
limpaTerminal()

ano = int(input('Digite o seu ano de nascimento: '))

if ano < 16:
    print('Você não tem idade para votar e muito menos tirar habilitação!')
elif ano >= 16 and ano < 18:
    print('Você pode votar, porém não pode tirar habilitação ainda!')
else:
    print('Você é obrigado a votar e pode tirar habilitação!')