#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m

altura = float(input('Qual a altura da parede em metros: '))
largura = float(input('Qual a largura da parede em metros: '))
area = altura * largura
print('A área da parede tem dimensão de {}x{} e sua área é {}m\u00B2'.format(altura,largura,area))
print('Para pintar a parede serão necessários {} litros de tinta.'.format(area/2))
