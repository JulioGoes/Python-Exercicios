# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é:
# equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer
# dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;


def verificaTriangulo(lado1, lado2, lado3):
    v1 = (lado1 + lado2) > lado3
    v2 = (lado2 + lado3) > lado1
    v3 = (lado3 + lado1) > lado2
    if v1 and v2 and v3:
        return True
    else:
        return False


def verificaTipoDeTriangulo(lado1, lado, lado3):
    if lado1 == lado2 == lado3:
        print("É um triângulo Equilátero!")
    elif (lado1 == lado2) or (lado3 == lado1) or (lado2 == lado3):
        print("É um triângulo Isósceles")
    else:
        print("É um triângulo Escaleno!")


print("Vamos descobrir o tipo do Triângulo!")
lado1 = float(input("Digite valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite valor do segundo lado do triângulo: "))
lado3 = float(input("Digite valor do terceiro lado do triângulo: "))
verifica = verificaTriangulo(lado1, lado2, lado3)

if verifica:
    verificaTipoDeTriangulo(lado1, lado2, lado3)
else:
    print("Os números digitados não correspondem a um triângulo!")
