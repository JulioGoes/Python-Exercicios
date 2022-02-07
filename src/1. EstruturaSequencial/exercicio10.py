# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.
# Fórmula: F = C x 1,8 + 32
celsius = float(input('Digite a temperatura em graus celsius: '))
fahren = (celsius * 1.8) + 32
print('A temperatura em graus Fahrenheit é de {}°'.format(fahren))
