# Faça um Programa que leia três números e mostre o maior deles.

lista = []
count = 1

for i in range(3):
    i = int(input(f'Digite {count}º número: '))
    lista.append(i)
    count += 1

valor_maior = min(lista)
print(f'O menor valor é {valor_maior}')
