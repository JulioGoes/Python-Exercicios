from random import randint

# Tamanho da Ilha
tamanho = ('pequena', 'pequena', 'pequena', 'media', 'media', 'grande')
# População de Monstros
populacao = ('baixa', 'baixa', 'media', 'media', 'media', 'alta')
# Tier
tier = ('1', '1', '2', '2', '2', '3')

ilhas = ('Aquatic/Underwater',
         'Artic',
         'Bandlands/Desert',
         'Coastal/Farmlands/Plains/Forest',
         'Feywild',
         'Grassland/Jungle/Tropical',
         'Hill/Mountain/Volcanic',
         'Marshes/Swamp',
         'Ruins/Shadowfell/Underdark/Underground',
         'Undead')


def retornaBioma(escolha_ilha):
    bioma_escolhido = 0

    if escolha_ilha <= 5:
        bioma_escolhido = ilhas[0]
    elif escolha_ilha > 5 and escolha_ilha <= 10:
        bioma_escolhido = ilhas[1]
    elif escolha_ilha > 10 and escolha_ilha <= 15:
        bioma_escolhido = ilhas[2]
    elif escolha_ilha > 15 and escolha_ilha <= 25:
        bioma_escolhido = ilhas[3]
    elif escolha_ilha > 25 and escolha_ilha <= 30:
        bioma_escolhido = ilhas[4]
    elif escolha_ilha > 30 and escolha_ilha <= 70:
        bioma_escolhido = ilhas[5]
    elif escolha_ilha > 70 and escolha_ilha <= 80:
        bioma_escolhido = ilhas[6]
    elif escolha_ilha > 81 and escolha_ilha <= 90:
        bioma_escolhido = ilhas[7]
    elif escolha_ilha > 90 and escolha_ilha <= 95:
        bioma_escolhido = ilhas[8]
    elif escolha_ilha > 95 and escolha_ilha <= 100:
        bioma_escolhido = ilhas[9]

    return bioma_escolhido


bioma = retornaBioma(randint(1, 100))

print('GERADOR DE ILHAS PARA VRO')
print('Tamanho da Ilha:       ', tamanho[randint(0, 5)].title())
print('População de Monstros: ', populacao[randint(0, 5)].title())
print('Tier da Ilha:          ', tier[randint(0, 5)])
print('Bioma da Ilha:         ', bioma)
