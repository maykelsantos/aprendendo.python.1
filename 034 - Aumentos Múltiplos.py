#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salário = float(input('Qual o salário do funcionário? '))
salário15 = salário + (salário * 0.15)
salário10 = salário + (salário * 0.10)
if salário <= 1250:
    print ('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f}'.format(salário, salário15))
if salário > 1250:
    print ('Quem ganhava R${:.2f} agora passa a ganhar R${:.2f}'.format(salário, salário10))
