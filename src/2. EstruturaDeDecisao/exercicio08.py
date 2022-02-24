# Faça um programa que pergunte o preço de três produtos
# e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

lista = []
count = 1

for i in range(3):
    preco = float(input(f'Digite o preço do {count}º produto: '))
    lista.append(preco)
    count += 1

melhor_preco = min(lista)
print(f'O melhor preço é {melhor_preco}')
