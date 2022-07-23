print('Fórmula para traço de concreto em volume')
quant = float(input('Qual a quantidade de traços a fazer?'))
agua = quant * 28
areia = quant * 3
brita = quant * 3
cim = quant
print('A quantidade certa, considerando a mesma medida é: \n'
      ' {:.1f} de cimento, {} de areia, {} de brita e {} de litros água'.format(cim, areia, brita, agua))
