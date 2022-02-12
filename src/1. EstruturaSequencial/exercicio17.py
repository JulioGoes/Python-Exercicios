# Faça um Programa para uma loja de tintas. O programa deverá
# pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6
# metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que
# custam R$ 25,00. Informe ao usuário as quantidades de tinta
# a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta
# seja menor. Acrescente 10% de folga e sempre arredonde os valores
# para cima, isto é, considere latas cheias.
from math import ceil

print('**LOJA DE TINTAS GOES**')
area_a_pintar = int(input('Área a ser Pintada em m²: '))

litros_usados = area_a_pintar / 6
print(litros_usados)
latas = ceil(litros_usados / 18)
galoes = ceil(litros_usados / 3.6)
custo_latas = 80.0 * latas
custo_galoes = 25.0 * galoes

print(f'LATAS NECESSÁRIAS: {latas:d} | CUSTO: R${custo_latas:.2f}')
print(f'GALÕES NECESSÁRIOS: {galoes:d} | CUSTO: R${custo_galoes:.2f}')

print('*****************************')
print('PARA EVITAR DESPERDÍCIO DE TINTA, SUGERIMOS O SEGUINTE')

contador = 0
while litros_usados > 0:
    litros_usados -= 3.6
    contador += 1

if contador == 1:
    print(f'COMPRE {galoes} GALÃO')
elif contador <= 5:
    print(f'COMPRE {contador} GALÕES')
elif contador == 6:
    print(f'COMPRE {latas - 1} LATA')
elif contador > 6 and contador < 12:
    print(f'COMPRE {latas - 1} LATA E {galoes - 5} GALÕES')
else:
    print(f'COMPRE {latas} LATAS')
