#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# primeiro forma de realizar este exercício
import math
angulo = float(input('Digite o ângulo que você deseja: '))
# Necessário tranformar o graus em radiando, para isso utilizar a função 'radians'.
seno = math.sin(math.radians(angulo))
print ('O ângulo de {} tem o SENO de {:.2f}.'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print ('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print ('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))
# segunda forma de realizar este exercício
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print ('O ângulo de {} tem o SENO DE {:.2f}.'.format(angulo, seno))
print ('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo, cosseno))
print ('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tangente))
