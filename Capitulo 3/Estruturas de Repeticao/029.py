# Uma agência de publicidade quer prestar serviços somente
# para as maiores companhias - em número de funcionários -
# em cada uma das classificações: grande, média, pequena e
# microempresa. Para tal, consegue um conjunto de dados com
# o código, o número de funcionários e o porte da empresa.

# Construa um algoritmo que liste o código da empresa com
# maiores recursos humanos dentro de sua categoria. Utilize
# como finalizador o código de empresa igual a 0.

from clean import limpaTerminal
limpaTerminal()

grande, medio, pequeno, microempresa = 0, 0, 0, 0
codGrande, codMedio, codPequeno, codMicroempresa = 0, 0, 0, 0
print('===== LISTANDO EMPRESAS ======')
while True:
    
    print('\nPORTE\n[1] - Grande\n[2] - Médio\n[3] - Pequeno\n[4] - Microempresa')
    porte = int(input(''))
    numPessoas = int(input('NÚMERO DE PESSOAS: '))
    cod = int(input('CÓDIGO: '))

    if cod == 0:
        break
    else:
        match(porte):
            # Grande
            case 1:
                if numPessoas > grande:
                    grande = numPessoas
                    codGrande = cod
            # Médio
            case 2:
                if numPessoas > medio:
                    medio = numPessoas
                    codMedio = cod
            # Pequeno
            case 3:
                if numPessoas > pequeno:
                    pequeno = numPessoas
                    codPequeno = cod
            # Microempresa
            case 4:
                if numPessoas > microempresa:
                    microempresa = numPessoas
                    codMicroempresa = cod
            case _:
                print('\nPORTE INVÁLIDO!')
                continue

print('\nGRANDE')
print(f'RH: {grande}\nCOD: {codGrande}')
print('\nMÉDIO')
print(f'RH: {medio}\nCOD: {codMedio}')
print('\nPEQUENO')
print(f'RH: {pequeno}\nCOD: {codPequeno}')
print('\nMICROEMPRESA')
print(f'RH: {microempresa}\nCOD: {codMicroempresa}')