#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str (input ('Informe seu nome: ')).strip()

print ('Existe SILVA em seu nome? {}'.format ('SILVA' in nome.upper()))
