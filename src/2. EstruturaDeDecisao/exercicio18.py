"""
Faça um Programa que peça uma data no formato dd/mm/aaaa
e determine se a mesma é uma data válida.
"""
import re
data = input("Digite um data no formato dd/mm/aaaa: ")
padrao = "[0-9]{2}/[0-9]{2}/[0-9]{4}"
retorno = re.findall(padrao, data)
print(retorno)
