#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math

# from math import hypot se vc quiser so usar uma funçao

co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
print ('A hipotenusa é {:.2f}'. format(math.hypot(co, ca)))

#outra forma
'''co = float(input('Qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
hi = (co ** 2 + ca ** 2) ** (1/2) #para calcula a raiz quadra 1/2
print ('A hipotenusa é {:.2f}'.format(hi))'''