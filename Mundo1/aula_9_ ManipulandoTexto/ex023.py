#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digítos separados.
    # EX: DIGITE UM NUMERO: 1834
    # unidade: 4
    # dezena: 3
    # centena: 8
    # milhar: 1
    
'''numero = str(input('Digite um número: '))

print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))'''

numero = int(input('Digite um número: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Exite uma maneira elegante usando a zfill
'''numero = input('Digite um número: ').zfill(4)

print('Unidade:', numero[3])
print('Dezena:', numero[2])
print('Centena:', numero[1])
print('Milhar:', numero[0])'''