# João Papo-de-Pescador, homem de bem, comprou um microcomputador
# para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00
# por quilo excedente. João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
quilos_totais = float(input('João, informe quantos kg pescou hoje: '))
limite = 50.0
multa = 4.0
excesso = 0.0
if (quilos_totais > limite):
    excesso = quilos_totais - limite
    multa = multa * excesso
    print('Temos um excesso de {}kg, a multa será de ${:.2f}'.format(excesso,
          multa))
else:
    print('Não ouve excesso hoje, tudo em ordem João o/')
