#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


from time import sleep
velocidade = float(input('Qual a sua velocidade atual? '))
print ('PROCESSANDO...')
sleep (2)
if velocidade > 80:
    print ('MULTADO! Você excedeu o limite de velocidade permitido que é 80km/h')
    multa = (velocidade-80)*7
    print ('Você precisará pagar uma taxa de R${:.2f}. Caso contrário, seu carro será apreendido!'.format(multa))
else:
    print ('Tenha uma boa viagem e dirija com cuidado!')
