import random

textred = '\033[31m'
textgreen = '\033[32m'
textblue = '\033[36m'
limpa = '\033[m'

escolha = int(input('Escolha um número de 0 a 5: {}'.format(textblue)))
num = random.randint(0,5)

if escolha == num:
    print('{}{}Você acertou!{}'.format(limpa,textgreen,limpa))
else:
    print('{}{}Você errou...{}'.format(limpa,textred,limpa))
    print('O certo era {}{}{}'.format(textgreen,num,limpa))
