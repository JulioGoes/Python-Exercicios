# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
print('Vamos descobrir quanto foi seu salário no último mês!')
por_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou no último mês? '))
salario = por_hora * horas_trabalhadas
print('Seu salário no último mês foi de ${}'.format(salario))
