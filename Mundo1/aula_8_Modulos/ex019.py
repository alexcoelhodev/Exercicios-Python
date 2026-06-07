#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o noem do terceiro aluno: '))
a4 = str(input('Digite o nome do terceiro aluno: '))
import random

print ('O aluno escolhido foi o {}'.format(random.choice([a1,a2,a3,a4])))

# esse jeito abaixo é mais descritivo e inicial
'''import random
a1= str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3= str(input('Digite o noem do terceiro aluno: '))
a4= str(input('Digite o nome do terceiro aluno: '))
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)

print ('O aluno escolhido foi o {}'.format(escolhido))'''

# essa forma é mais simples para vc não digitar em cada linha
'''from random import choice
alunos = input('Escreva o nome dos alunos separados por vírgula: ').split(", ")
print('O aluno escolhido foi: {}'.format(choice(alunos)))'''
