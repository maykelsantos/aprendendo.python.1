#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

from time import sleep
print ('+'*50)
km = float(input('Me informe a distância em KM da sua viagem: '))
print ('+'*50)
print ('CALCULANDO TRAJETO ...')
sleep (2)
if km <= 200:
    valor = 0.5 * km
    print ('Sua viagem custará um total de R${:.2f}'.format(valor))
else:
    valor = 0.45 * km
    print ('Sua viagem custará R${:.2f}'.format(valor))
