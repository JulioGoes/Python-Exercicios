# As Organizações Tabajara resolveram dar um aumento de salário
# aos seus colaboradores e lhe contrataram para desenvolver o programa
# que calculará os reajustes. Faça um programa que recebe o salário de
# um colaborador e o reajuste segundo o seguinte critério, baseado no
# salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser
# realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
import os
os.system('clear')

print('As Organizações Tabajara lhe concederá um aumento salarial!')
salario = float(input('Por gentileza, informe seu salário atual: '))
aumento = 0.0


def imprime(salario, porcentual, valor_do_aumento, salario_final):
    print(f'Salário Anterior: {salario}')
    print(f'Porcentual Aplicado: {porcentual}')
    print(f'Valor do Aumento: {valor_do_aumento:.2f}')
    print(f'Novo Salário: {salario_final:.2f}')


if salario <= 280.00:
    aumento = 0.20
    porcentual = '20%'
    valor_do_aumento = salario * aumento
    salario_final = salario + valor_do_aumento
    imprime(salario, porcentual, valor_do_aumento, salario_final)
elif salario <= 700.00 and salario > 281.00:
    aumento = 0.15
    porcentual = '15%'
    valor_do_aumento = salario * aumento
    salario_final = salario + valor_do_aumento
    imprime(salario, porcentual, valor_do_aumento, salario_final)
elif salario <= 1500.00 and salario > 701.00:
    aumento = 0.10
    porcentual = '10%'
    valor_do_aumento = salario * aumento
    salario_final = salario + valor_do_aumento
    imprime(salario, porcentual, valor_do_aumento, salario_final)
elif salario > 1500.00:
    aumento = 0.05
    porcentual = '05%'
    valor_do_aumento = salario * aumento
    salario_final = salario + valor_do_aumento
    imprime(salario, porcentual, valor_do_aumento, salario_final)
