# Faça um Programa que leia três
# números e mostre-os em ordem decrescente.

valores = []
decre = []
count = 1
indice = 0

for i in range(3):
    valor = float(input(f'Digite o {count}º valor: '))
    valores.append(valor)
    count += 1

for i in range(3):
    num = max(valores)
    indice = valores.index(num)
    valor_removido = valores.pop(indice)
    decre.append(int(valor_removido))

print(f'Ordem Decrescente: {decre[0]}, {decre[1]} e {decre[2]}')
