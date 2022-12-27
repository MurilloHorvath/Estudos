textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

a = float(input('Digite o comprimento da primeira reta: {}'.format(textyellow)))
b = float(input('{}Digite o comprimento da segunda reta: {}'.format(limpa,textyellow)))
c = float(input('{}Digite o comprimento da terceira reta: {}'.format(limpa,textyellow)))

if a+b > c and a+c > b and b+c > a:
    print('{}{}Pode ser um triangulo{}'.format(limpa,textgreen,limpa))
else:
    print('{}{}Não pode ser um triangulo{}'.format(limpa,textred,limpa))
