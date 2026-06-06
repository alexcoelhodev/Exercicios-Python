# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele
n = input ('Digite Algo: ')
print ('O tipo primitivo desse valor é {}'.format(type(n)))
print ('Só tem espaços? {}'.format(n.isspace()))
print ('É um número? {}'.format(n.isnumeric()))
print ('É alfabeto? {}'.format(n.isalpha()))
print ('Está em maiusculas? {}'.format(n.isupper()))
print ('Está em minusculas? {}'. format(n.islower()))
print ('Esta capitalizada ou caixa alta? {}'.format(n.istitle()))