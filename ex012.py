print('Calculando o desconto!')
prod = float(input('Qual o valor do produto?'))
desc = float(input('Qual o valor do desconto(só o número)? '))
print('O produto de {}reais recebeu o desconto de {}%, e o valor dele ficou R${}'.format(prod, desc, prod-((desc/100)*prod)))