#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float (input ('Informe os quilometros percorrido: '))
dias = int (input ('Informe o total de dias alugados: '))
custodia = 60 * dias
custokm = 0.15 * km

print ('O valor total a ser pago pelo nosso serviço é de R${:.2f}'.format (custodia + custokm))
