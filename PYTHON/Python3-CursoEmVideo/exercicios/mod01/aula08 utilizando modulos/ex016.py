'''from math import trunc
num = float(input('Digite um número quebrado:'))
print('O número {} tem a parte inteira {}.'.format(num,trunc(num)))'''

textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

num = float(input('Digite um valor real: {}'.format(textred)))
print('{}O valor digitado {}{}{} e a sua porção inteira é {}{}{}'.format(limpa,textred,num,limpa,textgreen,int(num),limpa))
