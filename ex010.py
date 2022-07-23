print('Conversor de moeda!')
dol = 5.46
lib = 6.45
real = float(input('Quantos reais você tem? R$'))
print('Você tem {} reais.\n valor do dólar: {}\n valor das libras esterlinas: {}\n Você pode comprar {:.2f} dólares,\n ou {:.2f} libras esterlinas.'.format(real,dol,lib,real/dol, real/lib))