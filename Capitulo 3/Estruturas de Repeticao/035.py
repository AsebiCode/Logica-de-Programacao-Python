# Em um prédio há três elevadores, denominados A, B e C.
# Para otimizar o sistema de controle dos elevadores, foi
# realizado um levantamento no qual cada usuário respondia:
# - o elevador que utilizava com mais frequência;
# - o período em que utilizava o elevador, entre
#   - 'M' - matutino;
#   - 'V' - vespertino;
#   - 'N' - noturno.

# Construa um algoritmo que calcule e imprima:
# - qual é o elevador mais frequentado e em que período se
# concentra o maior fluxo;
# - qual é o período mais usado de todos e a qual elevador pertence;
# - qual é a diferença porcentual entre o mais usado dos
# horários e o menos usado;
# - qual é a porcentagem sobre o total de serviços prestados
# do elevador de média.

from clean import limpaTerminal
limpaTerminal()

# Contadores de uso por elevador
usoA, usoB, usoC = 0, 0, 0
# Contadores por período
mA, vA, nA = 0, 0, 0
mB, vB, nB = 0, 0, 0
mC, vC, nC = 0, 0, 0

i = 1
while True:
    print(f"\n{i}º Pessoa")
    elevador = input('Qual o elevador mais utilizado?\n(A | B | C) ou D para sair: ').upper()
    if elevador == 'D':
        break

    periodo = input('Período que mais usa:\n(M | V | N): ').upper()

    if elevador == 'A':
        usoA += 1
        if periodo == 'M':
            mA += 1
        elif periodo == 'V':
            vA += 1
        elif periodo == 'N':
            nA += 1
    elif elevador == 'B':
        usoB += 1
        if periodo == 'M':
            mB += 1
        elif periodo == 'V':
            vB += 1
        elif periodo == 'N':
            nB += 1
    elif elevador == 'C':
        usoC += 1
        if periodo == 'M':
            mC += 1
        elif periodo == 'V':
            vC += 1
        elif periodo == 'N':
            nC += 1
    else:
        print('Elevador inválido!')
    i += 1

# Totais por período
totalM = mA + mB + mC
totalV = vA + vB + vC
totalN = nA + nB + nC
totalGeral = totalM + totalV + totalN

# Elevador mais utilizado
if usoA >= usoB and usoA >= usoC:
    elevadorMais = 'A'
    if mA >= vA and mA >= nA:
        periodoMais = 'Matutino'
    elif vA >= mA and vA >= nA:
        periodoMais = 'Vespertino'
    else:
        periodoMais = 'Noturno'
elif usoB >= usoA and usoB >= usoC:
    elevadorMais = 'B'
    if mB >= vB and mB >= nB:
        periodoMais = 'Matutino'
    elif vB >= mB and vB >= nB:
        periodoMais = 'Vespertino'
    else:
        periodoMais = 'Noturno'
else:
    elevadorMais = 'C'
    if mC >= vC and mC >= nC:
        periodoMais = 'Matutino'
    elif vC >= mC and vC >= nC:
        periodoMais = 'Vespertino'
    else:
        periodoMais = 'Noturno'

# Período mais e menos usado
maisUsado = max(totalM, totalV, totalN)
menosUsado = min(totalM, totalV, totalN)
difPorcento = ((maisUsado - menosUsado) * 100) / totalGeral

# Elevador de uso médio
if (usoA >= usoB and usoA <= usoC) or (usoA <= usoB and usoA >= usoC):
    elevadorMedio = 'A'
    usoMedio = usoA
elif (usoB >= usoA and usoB <= usoC) or (usoB <= usoA and usoB >= usoC):
    elevadorMedio = 'B'
    usoMedio = usoB
else:
    elevadorMedio = 'C'
    usoMedio = usoC
porcentagemMedio = (usoMedio * 100) / totalGeral

print(f"\n- Elevador mais utilizado: {elevadorMais}")
print(f"- Período de maior fluxo nesse elevador: {periodoMais}")
print(f"- Diferença porcentual entre período mais e menos usado: {difPorcento:.2f}%")
print(f"- Porcentagem de uso do elevador de média: {elevadorMedio} = {porcentagemMedio:.2f}%")
