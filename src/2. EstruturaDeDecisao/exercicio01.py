# Faça um Programa que peça dois números e imprima o maior deles.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}!')
elif num1 == num2:
    print('Os números são iguais!')
else:
    print(f'{num2} é maior que {num1}!')
