from random import randint

# Tier da Tripulação
tier = ('1', '1', '2', '2', '2', '3')
# Estado da Tripulação
estado = ('amigável', 'amigável', 'hostil', 'hostil', 'hostil', 'neutra')
# Tipo da Tripulação
tipo = ('mercantil/exploradora', 'mercantil/exploradora', 'morto-vivo',
        'bárbaros', 'pirate', 'pirata corja')

print('GERADOR DE TRIPULAÇÃO PARA VRO')
print('Tier:       ', tier[randint(0, 5)])
print('Estado:     ', estado[randint(0, 5)].title())
print('Tipo:       ', tipo[randint(0, 5)].title())
