# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
# fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo
# grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao
# usuário;
from math import sqrt

print("Vamos descobrir os valores da equação ax2 + bx + c")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
if a == 0:
    print("O valor de A é inválido!")
else:
    print(f"A equação ficou da seguinte maneira: {a}x² + {b}x + {c}")
    delta = ((pow(b, 2)) - (4 * a * c))
    if delta < 0:
        print(f"Valor de delta é {delta}, logo, a equação não possui raízes!")
    else:
        raiz_de_delta = sqrt(delta)
        divisor = 2 * a
        x1 = ((b * -1) + raiz_de_delta) / divisor
        x2 = ((b * -1) - raiz_de_delta) / divisor
        print(f"Logo, as raízes da equação são: {x1} e {x2}")
