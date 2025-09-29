textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

num = int(input('Digite um número: {}'.format(textyellow)))

teste = num % 2

if teste == 0:
    print('{}{}PAR{}'.format(limpa,textgreen,limpa))
else:
    print('{}{}IMPAR{}'.format(limpa,textred,limpa))
