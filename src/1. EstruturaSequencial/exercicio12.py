# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
print('Vamos descobrir seu peso ideal!')
altura = float(input('Digite sua altura: '))
peso_ideal = (72.7 * altura) - 58
print('Seu peso ideal é de {:.2f}'.format(peso_ideal))
