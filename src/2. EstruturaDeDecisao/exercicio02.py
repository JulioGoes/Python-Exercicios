# Faça um Programa que peça um valor e mostre na tela se o
# valor é positivo ou negativo.
num1 = float(input('Digite um número: '))

if num1 > 0:
    print(f'{num1} é um valor positivo!')
elif num1 == 0:
    print(f'{num1} é zero!')
else:
    print(f'{num1} é um valor negativo!')
