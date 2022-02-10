# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Vamos ver qual foi a sua média no ano letivo!')
sem1 = float(input('Digite sua nota no 1º Semestre: '))
sem2 = float(input('Digite sua nota no 2º Semestre: '))
sem3 = float(input('Digite sua nota no 3º Semestre: '))
sem4 = float(input('Digite sua nota no 4º Semestre: '))
media = (sem1 + sem2 + sem3 + sem4) / 4
print('Sua média no ano letivo foi de {}'.format(media))
