# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3_f = float(input('Digite um número real: '))
questao_a = (num1 * 2) * (num2 / 2)
print('O produto do dobro de {} com metade de {} é igual a {}'.format(num1,
      num2, (questao_a)))

questao_b = (num1 * 3) + num3_f
print('A soma do triplo do {} com o {} é igual a {}'.format(num1, num3_f,
      questao_b))

questao_c = pow(num3_f, 3)
print('{} elevado ao cubo é igual a {}'.format(num3_f, questao_c))
