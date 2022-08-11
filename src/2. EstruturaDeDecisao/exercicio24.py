# Faça um Programa que leia 2 números e em seguida
# pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga
# se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
num = float(input("Informe um número: "))
print("Qual operação deseja realizar?")
print("(A) Par/Impar | (B) Positivo/Negativo | (C) Inteiro/Decimal:")
escolha = input()

if escolha.upper() == "A":
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
elif escolha.upper() == "B":
    if num >= 0:
        print(f"{num} é positivo")
    else:
        print(f"{num} é negativo")
elif escolha.upper() == "C":
    if round(num) == num:
        print(f"{num} é um número inteiro")
    else:
        print(f"{num} é um número decimal")
else:
    print("Escolha Inválida")
