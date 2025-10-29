s= int(input('Qual o seu salário?'))
a= s*0.15
print('Então o seu novo salário com um aumento de 15% é R${:.2f}.'.format(s+a))
print('Então o seu novo salário com um aumento de 15% é R${:.2f}.'.format((s*0.15)+ s))