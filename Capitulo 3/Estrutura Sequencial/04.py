# Ao completar o tanque de combustível de um automóvel, faça um 
# algoritmo que calcule o consumo efetuado, assim como a autonomia 
# que o carro ainda teria antes do abastecimento. Considere que o 
# veículo sempre seja abastecido até encher o tanque e que sejam
# fornecidas apenas a capacidade do tanque, a quantidade de litros 
# abastecida e a quilometragem percorrida desde o último abastecimento.

from clean import limpaTerminal
limpaTerminal()

capacidadeTanque = float(input('Digite a capacidade do tanque: '))
litrosAbastecidos = float(input('Digite a quantidade de litros abastecidos: '))
kmPercorrido = float(input('Digite a quilometragem percorrida: '))

consumo = kmPercorrido / litrosAbastecidos
litrosConsumidos = capacidadeTanque - litrosAbastecidos
autonomia = litrosAbastecidos * consumo

print(f'\nConsumo: {consumo}\nLitros abastecidos: {litrosAbastecidos}\nAutonomia: {autonomia}')