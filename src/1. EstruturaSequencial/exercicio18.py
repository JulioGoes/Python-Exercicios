# Faça um programa que peça o tamanho de um arquivo para download
# (em MB) e a velocidade de um link de Internet (em Mbps), calcule
# e informe o tempo aproximado dedownload do arquivo usando este
# link (em minutos).
from math import ceil

tamanho_arquivo = int(input('DIGITE O TAMANHO DO ARQUIVO EM MB: '))
velocidade = int(input('DIGITE A VELOCIDADE DE DOWNLOAD EM MBPS: '))
tempo_de_download = tamanho_arquivo / velocidade
tempo_em_minutos = ceil(tempo_de_download / 60)
print(f'TEMPO APROXIMADO DE DOWNLOAD EM MINUTOS {tempo_em_minutos}')
