# primeira forma de realizar este exercício
import math
num = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua porção inteira foi {}.'.format(num, math.trunc(num)))
# segunda forma de realizar este exercício
from math import trunc
num = float(input('Digite um valor: '))
print ('O vaor digitado foi {} e a sua porção interia é {}.'.format(num, trunc(num)))
# terceira forma de realizar este exercício
num = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
