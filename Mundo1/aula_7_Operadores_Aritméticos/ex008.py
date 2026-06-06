#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = float(input('Digite uma distância em metros: '))
print('O valor que você digitou foi {} metro(s) \n Convertendo: \n Decímetro: {}dc \n Centímetros: {}cm \n Milímetros: {}mm \n Decâmetro: {}dam \n Hectômetro: {}hm \n Quilometro: {}km'.format(valor,(valor*10), (valor*100), (valor*1000), (valor/10), (valor/100), (valor/1000)))

# Abaixo vou escrever uma forma mais moderna e limpa

# valor = float(input('Digite uma distância em metros: '))
# print(f'''
# O valor digitado foi {valor} metro(s)
# Convertendo:
# Decímetro: {valor * 10} dm
# Centímetro: {valor * 100} cm
# Milímetro: {valor * 1000} mm
# Decâmetro: {valor / 10} dam
# Hectômetro: {valor / 100} hm
# Quilômetro: {valor / 1000} km
# ''')