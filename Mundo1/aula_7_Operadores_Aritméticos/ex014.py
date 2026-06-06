# Escreva um prgrama que converta uma temperatura digitada em Celsius para Fahrenheit
tempC = float(input('Informe a temperatura em Celsius: '))
tempF = (tempC * 9 / 5) + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(tempC, tempF))
