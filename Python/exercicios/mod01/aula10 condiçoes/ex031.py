textgreen = '\033[32m'
textyellow = '\033[33m'
textpurple = '\033[34m'
limpa = '\033[m'

dist = int(input('Qual a distância da viagem? {}'.format(textyellow)))

if dist>200:
    print('{}{}Viagem Longa...{}'.format(limpa,textpurple,limpa))
    preço = dist * 0.45
    print('Total a pagar {}R${:.2f}{}'.format(textgreen,preço,limpa))
else:
    print('{}{}Viagem normal...{}'.format(limpa,textpurple,limpa))
    preço = dist * 0.50
    print('Total a pagar {}R${:.2f}{}'.format(textgreen,preço,limpa))
print('Boa Viagem!')