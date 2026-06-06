#Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número inteiro: '))
print('O número digitado é {}, seu antecessor é {} e seu sucessor é {}.'.format(numero, (numero-1), (numero +1)))

#resposta do professor
# n = int(inout('Digite um número: '))
# a = n-1
# s = n +1
# print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.formart(n, a, s))

#Cada passo fica explícito no exemplo do professor então é melhor do que a forma direta que eu fiz
# 1) Mais fácil de entender para quem está começando
# 2) Facilita depuração e futuras mudanças
# 3) Segue o princípio de clareza > esperteza

#Exemplo de codigo mais profissional segundo IA
#def analisar_numero(numero: int) -> tuple[int, int]:
   # return numero - 1, numero + 1

#numero = int(input('Digite um número inteiro: '))
#antecessor, sucessor = analisar_numero(numero)

#print(f'Analisando o valor {numero}, seu antecessor é {antecessor} e o sucessor é {sucessor}.')
