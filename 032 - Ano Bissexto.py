#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para descobrir o ano atual: '))
if ano == 0:
    ano = date.today().year
    print ('O ano atual é {}.'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano {} é BISSEXTO.'.format(ano))
else:
    print ('O ano {} NÃO É BISSEXTO.'.format(ano))
