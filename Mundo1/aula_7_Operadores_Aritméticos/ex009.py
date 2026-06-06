#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Digite um numero para ver a sua tabuada: '))
print('O valor digitado foi {}, e sua tabuada é:'.format(numero))
print('____________________')
print('{} x {:2} = {:2}'.format(numero, 1, numero*1))
print('{} x {:2} = {}'.format(numero, 2, numero*2))
print('{} x {:2} = {}'.format(numero, 3, numero*3))
print('{} x {:2} = {}'.format(numero, 4, numero*4))
print('{} x {:2} = {}'.format(numero, 5, numero*5))
print('{} x {:2} = {}'.format(numero, 6, numero*6))
print('{} x {:2} = {}'.format(numero, 7, numero*7))
print('{} x {:2} = {}'.format(numero, 8, numero*8))
print('{} x {:2} = {}'.format(numero, 9, numero*9))
print('{} x {:2} = {}'.format(numero, 10, numero*10))
print('_'*20)

#Uma versão bem moderna e profissional com menos linha

#numero = int(input('Digite um numero para ver a sua tabuada: '))
#print(f'O valor digitado foi {numero}, e sua tabuada é:')
#print('____________________')
#for i in range(1, 11):
#    print(f'{numero} x {i} = {numero * i}')
#print('____________________')