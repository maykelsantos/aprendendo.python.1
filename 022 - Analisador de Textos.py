#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

frase = str(input('Qual o seu nome completo? ')).strip()
print ('Seu nome com todas as letras maiúsculas fica: {}'.format(frase.upper()))
print ('Seu nome com todas as letras minúsculas fica: {}'.format(frase.lower()))
print ('Seu nome tem {} letras no total.'.format(len(frase) - frase.count(' ')))
print ('Seu primeiro nome tem {} letras.'.format(frase.find(' ')))
separa = frase.split()
print ('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
