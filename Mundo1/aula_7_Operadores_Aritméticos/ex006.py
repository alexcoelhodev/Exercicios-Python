#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um número: '))
print('O numero digitado foi {}. \nO dobro deste número é {}, o triplo é {} e sua raiz quadrada é {:.2f}'.format(numero, numero*2, numero*3, numero**(1/2)))

# Quando voce digita \n voce pula a linha, colocando uma quebra
# para formatar o numero de casas decimais apos a virgula, dentro do {} vc coloca {:.2f} dois pontos, ponto, numero de casas flutuantes
# Voce pode calcular a potencia colocando pow (n, (1/2)
