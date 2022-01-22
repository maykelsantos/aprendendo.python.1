#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmeto: '))
seg3 = float(input('Digite o terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 +seg3 and seg3 < seg1 + seg2:
    print ('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print ('Os segmentos acima NÃO FORMAM um triângulo!')
