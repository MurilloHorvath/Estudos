'''
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipo = (co**2 + ca**2)**(1/2)
print('A hipotenusa do tringulo vai medir {:.2f}'.format(hipo))
'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipo = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
