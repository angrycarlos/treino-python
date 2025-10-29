from math import radians, sin, cos, tan
a=float(input('Digite um angulo: '))
r= radians(a)
print('Se o seu angulo é {:.3f}, então:\nSeno-> {:.3f}\nCosseno-> {:.3f}\nTangente-> {:.3f}.'.format(a, sin(r), cos(r), tan(r)))