# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

print('Em que turno você estuda?')
turno = input('(M) Matutino | (V) Vespertino | (N) Noturno: ')

if turno.lower() == 'm':
    print('Bom Dia!')
elif turno.lower() == 'v':
    print('Boa Tarde!')
elif turno.lower() == 'n':
    print('Boa Noite!')
else:
    print('Valor Inválido')
