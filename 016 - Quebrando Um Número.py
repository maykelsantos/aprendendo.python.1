#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

numero = float (input ('Informe um número real: '))

print ('O valor digitado foi {} e a sua porção inteira é {:.0f}'.format (numero, math.trunc (numero)))
