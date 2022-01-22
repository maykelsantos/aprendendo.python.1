#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float (input ('Informe a largura da parade: '))
altura = float (input ('Informe a altura da parede: '))
area = largura * altura
litro = 2

print ('A área de sua parede é {:.2f}m²'.format (area))
print ('E você precisará de {:.2f}l de tinta.'.format (area / litro))
