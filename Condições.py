# Primeira forma de realizar este exercício
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Seu carro é novo!')
else:
    print('Seu carro é antigo!')
# Segunda forma de realizar este exercício
tempo = int(input('Quantos anos tem o seu carro? '))
print ('Seu carro é novo!' if tempo <=3 else 'Seu carro é antigo!')
# A condição 'if' siginifica 'se'
# A condição 'else' significa 'senão'
# Não esqueçer dos ':' após cada condicional
# Não esquecer do 'TAB' na realização da condicional

# Condições Simples
nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Maykel':
    print ('Seu nome é muito lindo, {}. Seja muito bem vindo!'.format(nome))
else:
    print ('Seja bem vindo, {}.'.format(nome))

#Condições Compostas
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
media = (nota1+nota2)/2
print ('Sua média é {:.1f}'.format(media))
if media >=7:
    print ('Parabéns, você passou de ano!')
else:
    print ('Infelizmente você é burro!')
    