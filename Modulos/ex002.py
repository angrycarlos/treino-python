import math
cto=int(input('Digite o comprimento do cateto oposto: '))
cta=int(input('Digite o comprimento do cateto adjacente: '))
print('A sua hipotenusa é {}'.format(math.sqrt((pow(cto, 2)) + (pow(cta, 2)))))