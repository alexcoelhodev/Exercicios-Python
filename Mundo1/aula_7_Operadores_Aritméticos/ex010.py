#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere U$1.00 = R$3.27
dinheiro = int(input('Quanto de dinheiro você tem? '))
print('Convertendo esse valor para dolares, com o dolar a R$ 3.27, você terá para gastar R$ {:.2f} '.format(dinheiro*3.27))
