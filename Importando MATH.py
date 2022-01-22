import math
# 'math' significa matematica e 'import' importa a biblioteca especificada
n1 = int(input('Digite um número: '))
raiz = math.sqrt(n1)
# 'sqrt' importa somente a raiz quadrada de algo especificado em parênteses
print ('A raiz quadrada de {} é igual a {}.'.format(n1, math.ceil(raiz)))
# 'ceil' arrendonda o número importado para cima
# 'floor' arrenda o número importado para baixo 
