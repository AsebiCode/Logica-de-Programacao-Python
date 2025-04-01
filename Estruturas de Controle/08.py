# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# 1 -  À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 -  À vista no cartão de crédito, recebe 5% de desconto
# 3 -  Em duas vezes, preço normal de etiqueta sem juros
# 4 -  Em três vezes, preço normal de etiqueta mais juros de 10%

import clean
clean.limpaTerminal()

preco = float(input('Digite o preço normal de etiqueta do produto: '))

print('=' * 35)
print('| Nº |     Forma de Pagamento     |')
print('=' * 35)
print('| 1  | Dinheiro/Cheque (-10%)     |')
print('| 2  | Cartão à vista (-5%)       |')
print('| 3  | 2x Sem Juros               |')
print('| 4  | 3x (+10% de Juros)         |')
print('=' * 35)

codigo = int(input('\nDigite o código da forma de pagamento, conforme a tabela acima: '))

match(codigo):
    case 1:
        valorAPagar = preco - (preco * 0.10)
        print(f'\nValor a pagar: R${valorAPagar:.2f}')
    case 2:
        valorAPagar = preco - (preco * 0.05)
        print(f'\nValor a pagar: R${valorAPagar:.2f}')
    case 3:
        valorAPagar = preco / 2
        print(f'Valor da parcela (2x): R${valorAPagar:.2f}')
    case 4:
        valorAPagar = preco / 3
        print(f'Valor da parcela (3x): R${valorAPagar:.2f}')
    case _:
        print('Código inválido!')