# Faça um programa que faça 5 perguntas para
# uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final
# emitir uma classificação sobre a participação da pessoa
# no crime. Se a pessoa responder positivamente a 2 questões
# ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele
# será classificado como "Inocente".
print("JC, O INVESTIGADOR")
print("VOCÊ SERÁ SUBMETIDO A UM QUESTIONÁRIO ENVOLVENDO O CRIME DA")
print("MADAME ORLIA, RESPONDA APENAS COM 's' PARA SIM")
print("E 'n' PARA NÃO")
count = 0


def contadorDeCulpa(resposta, count):
    if resposta == 's':
        count += 1
    return count


resposta = input("TELEFONOU PARA A VÍTIMA? ")
count = contadorDeCulpa(resposta, count)

resposta = input("ESTEVE NO LOCAL DO CRIME? ")
count = contadorDeCulpa(resposta, count)

resposta = input("MORA PERTO DA VÍTIMA? ")
count = contadorDeCulpa(resposta, count)

resposta = input("DEVIA PARA A VÍTIMA? ")
count = contadorDeCulpa(resposta, count)

resposta = input("JÁ TRABALHOU PARA A VÍTIMA? ")
count = contadorDeCulpa(resposta, count)

if count == 5:
    print("TEJE PRESO, VOCÊ É O CULPADO!")
elif count == 3 or count == 4:
    print("TEJE PRESO, VOCÊ É UM CÚMPLICE!")
elif count == 2:
    print("É UM SUSPEITO EM POTENCIAL")
else:
    print("Você é inocente... compreensível, tenha um bom dia.")