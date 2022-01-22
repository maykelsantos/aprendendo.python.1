# primeira forma de realizar este exercício
import random
# 'RANDOM' siginifica aleatório
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
# 'SHUFFLE' siginifica embaralhar
print ('A ordem de apresentação será: {}.'. format(lista))
# segunda forma de realizar este exercício
from random import shuffle
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print ('A ordem de apresentaçã será: '.format(lista))
