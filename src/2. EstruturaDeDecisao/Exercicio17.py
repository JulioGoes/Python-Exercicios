'''
Faça um Programa que peça um número correspondente a um determinado
ano e em seguida informe se este ano é ou não bissexto.
'''

anos = ['1500', '1600', '1700', '1800', '1900', '2000', '2100']


def checa_ano(resultado):
    ultimos_numeros_str = str(resultado)
    casa_pos_ponto = ultimos_numeros_str.find('.')
    numeros_pos_ponto = ultimos_numeros_str[casa_pos_ponto + 1:]
    if numeros_pos_ponto == '0':
        print('Bissexto')
    else:
        print('Não Bissexto')


for ano in anos:
    ultimos_numeros = ano[2:]
    if str(ultimos_numeros) == '00':
        resultado = int(ano) / 400
        checa_ano(resultado)
    else:
        resultado = int(ultimos_numeros) / 4
        checa_ano(resultado)
