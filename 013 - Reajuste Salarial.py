#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float (input ('Informe seu salário atual: R$'))
aumento = salario * 0.15

print ('Seu novo salário é de R${:.2f}'.format (salario + aumento))
