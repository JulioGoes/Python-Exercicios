'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima
a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
import os

os.system('clear')
num = input('Digite um número inteiro menor que 1000: ')
if num.isnumeric() and int(num) < 1000:
    unidade = num[-1]
    if int(num) < 10:
        print(f'Unidade: {unidade}')
    elif int(num) >= 10 and int(num) < 100:
        dezena = num[-2]
        print(f'Dezena: {dezena} | Unidade: {unidade}')
    elif int(num) >= 100:
        dezena = num[-2]
        centena = num[-3]
        print(f'Centena: {centena} | Dezena: {dezena} | Unidade: {unidade}')
else:
    print('Valor Digitado Incorreto')
