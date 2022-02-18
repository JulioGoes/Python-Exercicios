# Faça um programa que lê as duas notas parciais obtidas por um
# aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
# onceito for D ou E.
print("Vamos descobrir se você foi aprovado na disciplina!")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 9.0 and media <= 10.0:
    print(f"Sua nota foi {media}! Você tirou um A e foi Aprovado!")
elif media >= 7.5 and media < 9:
    print(f"Sua nota foi {media}! Você tirou um B e foi Aprovado!")
elif media >= 6.0 and media < 7.5:
    print(f"Sua nota foi {media}! Você tirou um C e foi Aprovado!")
elif media >= 4.0 and media < 6.0:
    print(f"Sua nota foi {media}! Você tirou um D e foi Reprovado!")
elif media > 0 and media < 4.0:
    print(f"Sua nota foi {media}! Você tirou um E e foi Reprovado!")
else:
    print("Você digitou valores inválidos!")
