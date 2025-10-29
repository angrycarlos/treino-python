c=int(input('Qual a temperatura em graus C°?'))
print('Se a sua temperatura é {}C°, então você tem {:.1f}F° e {:.2f}K°.'.format(c, ((c*1.8)+ 32), c + 273.15 ))