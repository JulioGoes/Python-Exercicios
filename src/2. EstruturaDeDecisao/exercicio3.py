# Faça um Programa que verifique se uma letra digitada é
# "F" ou "M". Conforme a letra escrever: F - Feminino, M
# - Masculino, Sexo Inválido.
print('Vamos verificar se uma pessoa é do sexo feminino ou masculino!')
condicao = input("Digite (F) ou (M): ")

if condicao.upper() == 'M':
    print('Sexo Masculino!')
elif condicao.upper() == 'F':
    print('Sexo Feminino!')
else:
    print('Sexo Inválido!')
