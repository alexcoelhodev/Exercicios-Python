#Crie um programa que leia um néumero real qualquer e mostre na tela a sua porção inteira
#import math

#num1 = float(input("Digite um número: "))
#print('O número digitado foi {} e sua parte inteira é {}'.format(num1, math.trunc(num1)))

# outra forma importando so a funçao necessária

'''from math import trunc
num1 = float(input('Digite um número: '))
print ('O número digitado foi {} e sua parte inteira é {}'. format(num1, trunc(num1)))'''

#quando vc coloca tres aspas no começo e no final o codigo para de funcionar

# Outra forma é usando uma funçao interna
num = float (input('Digite um valor: '))
print ('O valor digitado foi {} e sua porçao inteira é {}'.format(num, int(num)))
