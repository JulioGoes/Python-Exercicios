# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# Fórmula: C = 5 * ((F-32) / 9).
fahren = float(input('Digite a temperatura em Fahrenheit: '))
celsius = ((fahren - 32) / 9) * 5
print('A temperatura em graus celsius é de {}°'.format(celsius))
