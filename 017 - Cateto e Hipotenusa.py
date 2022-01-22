#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# primeira forma de reaizar este exercício
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**(0.5)
print ('A hipotenusa mede {:.2f}.'.format(hi))
#segunda forma de realizar este exercício
import math
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print ('A hipitenusa mede {:.2f}.'.format(hi))
# terceira forma de realizar este exercício
from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print ('A hipotenusa mede {:.2f}.'.format(hi))
       