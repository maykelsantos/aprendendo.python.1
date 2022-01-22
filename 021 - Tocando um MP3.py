import pygame
# precisamos iniciar a biblioteca com o comando 'init'
pygame.init()
# necessário o arquivo mp3 está carregado no workspace
pygame.mixer.music.load('Arrebatamento.mp3')
pygame.mixer.music.play()
pygame.event.wait()
