print('Convertendo temperaturas')
c = float(input('Qual a temperatura para conversão?'))
f = c * 1.8 + 32
k = c + 273
print('A temperatura de {}°c \n Essa mesma temperatura em Fahrenheit é {}°F \n E em Kelvin é {}°k'.format(c,f,k))