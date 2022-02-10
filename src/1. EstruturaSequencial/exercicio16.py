# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da
# tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de
# latas de tinta a serem compradas e o preço total.
from math import ceil

print('**LOJA DE TINTAS GOES**')
area_a_pintar = int(input('Área a ser Pintada em m²: '))

litros_usados = area_a_pintar / 3
galoes = ceil(litros_usados / 18)
custo = 80.0 * galoes

print(f'GALÕES NECESSÁRIOS: {galoes:d} | CUSTO: R${custo:.2f}')
