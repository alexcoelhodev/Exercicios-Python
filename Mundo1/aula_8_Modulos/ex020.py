# O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Dgite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do terceiro aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)