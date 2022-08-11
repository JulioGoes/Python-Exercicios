from random import randint

# Dificuldade da Missão
dificuldade = ('D', 'D', 'D', 'C', 'C', 'B', 'B', 'A')

# Faccção da Missão
faccao = ('None', 'None', 'CND', 'ATA', 'GDV', 'ALC')

print('\nGERADOR DE MISSÕES PARA AeV\n')
print('Dificuldade:       ', dificuldade[randint(0, 5)])
print('Facção:            ', faccao[randint(0, 5)])
