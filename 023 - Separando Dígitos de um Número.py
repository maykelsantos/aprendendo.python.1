#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Primeira forma de realizar este exercício
numero = int(input('Informe um número de 0 a 9999: '))
strnumero = str(numero)
print ('A unidade é: {}'.format(strnumero[3]))
print ('A dezena é: {}'.format(strnumero[2]))
print ('A centena é: {}'.format(strnumero[1]))
print ('O milhar é: {}'.format(strnumero[0]))
# Segunda forma de realizar este exercício
numero = int(input('Informe um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print ('A unidade é: {}'.format(unidade))
print ('A dezena é: {}'.format(dezena))
print ('A centena é: {}'.format(centena))
print ('O milhar é: {}'.format(milhar))