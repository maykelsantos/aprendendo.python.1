frase = 'Jesus Te Ama'
print (len(frase))
# A função 'len' tem origem da palavra 'LENGTH' que siginifica 'COMPRIMENTO'. Sendo assim, a função acima traz o números de caracteres apartir de 0
print (frase.count('s'))
# A função 'count' conta quantos caracteres especificados em aspas existem. Não esqueça que o Python diferencia letras maiúsculas de minúsculas
print (frase.count('s',0,12))
# A sintaxe acima realiza uma análise juntamente com fatiamento
print (frase.find('Te'))
# A função 'find' encontra onde começou os caracteres especificados entre aspas
print (frase.find('Louco'))
# Quando a função 'find' não encontra os caracteres especificados entre aspas, ela retorna '-1'
print ('Ama' in frase)
# A função 'in' retorna 'verdadeiro' ou 'falso' para caracteres especificado entre aspas
