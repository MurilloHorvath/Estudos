'''
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipo = (co**2 + ca**2)**(1/2)
print('A hipotenusa do tringulo vai medir {:.2f}'.format(hipo))
'''

textred = '\033[31m'
textgreen = '\033[32m'
textpink = '\033[35m'
limpa = '\033[m'

from math import hypot
co = float(input('Digite o valor do cateto oposto: {}'.format(textred)))
ca = float(input('{}Digite o valor do cateto adjacente: {}'.format(limpa,textgreen)))
hipo = hypot(co, ca)
print('{}A hipotenusa vai medir {}{:.2f}{}'.format(limpa,textpink,hipo,limpa))
