#Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo
'''import math

angulo = float(input('Digite um angulo: '))
print ('O angulo de {} tem o SENO de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print ('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print ('O angulo de {} tem TANGENTE de {:.2f}'. format(angulo, math.tan(math.radians(angulo))))'''

from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo: '))
print ('O angulo de {} tem o SENO de {:.2f}'.format(angulo, sin(radians(angulo))))
print ('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos(radians(angulo))))
print ('O angulo de {} tem TANGENTE de {:.2f}'. format(angulo, tan(radians(angulo))))

#se voce usar direto o from math vc deve tirar toda ref a math do codigo
#o seno, cos, tan esta em radians entao vc precisa usar esse radians para converter