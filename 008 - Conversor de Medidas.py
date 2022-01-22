#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float (input ('Informe a medida em metros: '))
cm = medida * 100
mm = medida * 1000

print ('A medida de {}m corresponde a medida de {}cm e {}mm'.format (medida, cm, mm))
