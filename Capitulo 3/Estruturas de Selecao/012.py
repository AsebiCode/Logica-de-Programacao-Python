# Construa um algoritmo que seja capaz de concluir qual
# dentre os seguintes animais foi escolhido, através de perguntas 
# e respostas. Animais possíveis: leão, cavalo, homem, macaco, morcego, 
# baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.

# Exemplo: É mamífero? Sim. É quadrupede? Sim. É carnívoro? Não. É herbivoro? Sim.
# Então o animal escolhido foi o cavalo.

from clean import limpaTerminal
limpaTerminal()

print('Vamos tentar descobrir seu animal!\n Por favor, responda com S/N.')

# MAMÍFERO
r = input('\nÉ mamífero? ')
if r in 'sS':
    # Quadrúpede
    r = input('É quadrúpede? ')
    if r in 'sS':
        # Carnívoro
        r = input('É carnívoro? ')
        if r in 'sS':
            print('\n É um leão!')
        # Herbívoro
        else:
            print('\nÉ um cavalo!')
    #Bípede
    else:
        r = input('É bípede? ')
        if r in 'sS':
            #Onívoro
            r = input('É onívoro? ')
            if r in 'sS':
                print('\nÉ um homem!')
            # Frutívoro
            else:
                print('\nÉ um macaco!')
        # Voadores
        else:
            r = input('É voador? ')
            if r in 'sS':
                print('\nÉ um morcego!')
            # Aquático
            else:
                print('\nÉ uma baleia!')
# AVES
else:
    r = input('É ave? ')
    if r in 'sS':
        # Não Voadores
        r = input('É não voador? ')
        if r in 'sS':
            # Tropicais
            r = input('É tropical? ')
            if r in 'sS':
                print('\nÉ um avestruz!')
            # Polares
            else:
                print('\nÉ um pinguim!')
        # Nadadoras
        else:
            r = input('É nadador? ')
            if r in 'sS':
                print('\nÉ um pato!')
            # Rapina
            else:
                print('\nÉ uma águia!')
    # RÉPTEIS
    else:
        r = input('É réptil? ')
        if r in 'sS':
            # Com Casco
            r = input('É com casco? ')
            if r in 'sS':
                print('\nÉ uma tartaruga!')
            # Carnívoro
            else:
                r = input('É carnívoro? ')
                if r in 'sS':
                    print('\nÉ um crocodilo!')
                # Sem Patas
                else:
                    print('\nÉ uma cobra!')
        else:
            print('\nNenhum animal!')