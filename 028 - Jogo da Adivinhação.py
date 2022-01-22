#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador pensar
print ('De um número de 0 à 5...')
jogador = int(input('...Em que número eu pensei? ')) # Jogador tenta adivinhar
print ('COMPARANDO OS VALORES ...')
sleep(3)
if jogador == computador:
    print ('Eu pensei exatamente neste número. Parabéns, você me venceu!')
else:
    print ('Você perdeu! Eu pensei no número {} e não no número {}'.format(computador, jogador))
