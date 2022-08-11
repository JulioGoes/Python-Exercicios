# Faça um Programa para um caixa eletrônico. O programa deverá perguntar
# ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o
# máximo de 600 reais. O programa não deve se preocupar com a quantidade
# de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
# notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
# notas de 100, uma nota de 50, quatro notas de 10,
# uma nota de 5 e quatro notas de 1.
print("***CAIXA ELETRÔNICO***")
saque = int(input("Informe o valor do saque: "))
n_cem = 0
n_cinq = 0
n_vint = 0
n_dez = 0
n_cinco = 0
n_um = 0

while saque > 0:
    if saque >= 100:
        saque -= 100
        n_cem += 1
    if saque < 100 and saque >= 50:
        saque -= 50
        n_cinq += 1
    if saque < 50 and saque >= 20:
        saque -= 20
        n_vint += 1
    if saque < 20 and saque >= 10:
        saque -= 10
        n_dez += 1
    if saque < 10 and saque >= 5:
        saque -= 5
        n_cinco += 1
    if saque < 5 and saque >= 1:
        saque -= 1
        n_um += 1
print(f"Notas: {n_cem, n_cinq, n_vint, n_dez, n_cinco, n_um}")
print(f'resto: {saque}')
