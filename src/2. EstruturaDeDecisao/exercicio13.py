# Faça um Programa que leia um número e exiba o dia correspondente
# da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor
# deve aparecer valor inválido.
dias_da_semana = [
    'domingo',
    'segunda-feira',
    'terça-feira',
    'quarta-feira',
    'quinta-feira',
    'sexta-feira',
    'sábado'
]
dia = int(input("Digite um número de 1 a 7: "))
if dia >= 1 and dia <= 7:
    print(f'O número {dia} corresponde à {dias_da_semana[dia - 1]}')
else:
    print('Você digitou um valor inválido')
