#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# primeira fomra de realizar este exercício
import random
# 'RANDOM' siginifica aleatório
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
# Sempe usar conchetes para uma determinada lista
escolhido = random.choice(lista)
print ('O aluno escolhido foi o {}.'.format(escolhido))
# segunda forma de realizar este exercício
from random import choice
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print ('O aluno escolhido foi o {}.'.format(escolhido))
