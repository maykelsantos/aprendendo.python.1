#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float (input ('Informe quanto dinheiro você tem na carteira: R$'))
dolar = 5.2

print ('Você pode comprar U${:.2f}'.format (dinheiro / dolar))
