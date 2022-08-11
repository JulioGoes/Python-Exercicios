# Faça um Programa que peça um número e informe se o número é inteiro ou
# decimal.
# Dica: utilize uma função de arredondamento.

num = float(input("Informe um número: "))
if round(num) == num:
    print(f"{num} é número inteiro")
else:
    print(f"{num} [e um número decimal")
