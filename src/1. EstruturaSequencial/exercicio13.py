# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
print('Vamos descobrir seu peso ideal!')
genero = input('Primeiro me diga, você é homem (H) ou mulher (M)? ')
altura = float(input('Digite sua altura: '))
peso_ideal = 0.0
if (genero.upper() == 'H'):
    peso_ideal = (72.7 * altura) - 58
elif (genero.upper() == 'M'):
    peso_ideal = (62.1 * altura) - 44.7
print('Seu peso ideal é de {:.2f}'.format(peso_ideal))
