# ANSI : ESCAPE SEQUENCE
# STYLE: 0 'none', 1 'bold/negrito', 4 'underline/sublinhado', 7 'negative/inverter'
# TEXT: 30 'branco, 31 'vermelho', 32 'verde', 33 'amarelo', 34 'azul', 35 'lilás', 36 'azul piscina', 37 'cinza'
# BACK: 40 'branco', 41 'vermelho', 42 'verde', 43 'amarelo', 44 'azul', 45 'lilás', 46 'azul piscina', 47 'cinza'

print('\033[33;44mOlá, Mundo!\033[m')

a = 123
b = 321
print ('O valor de A é \033[33;42m{}\033[m e o valor de B é \033[32;43m{}\033[m ...'.format(a, b))

nome = 'Maykel'
print ('Prazer em te conhecer {}{}{}!!! Jesus te ama!'.format('\033[33;42m', nome, '\033[m'))
