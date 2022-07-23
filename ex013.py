print('Algoritmo para aumento dos salários')
sal = float(input('Qual o valor do salário?'))
porc = float(input('Qual a porcentagem de aumento(apenas números)?'))
salF = sal + (porc/100) * sal
print('O salário antigo é R${}. O novo salário é de {}'.format(sal,salF))
