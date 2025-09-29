textred = '\033[31m'
textgreen = '\033[32m'
textpurple = '\033[34m'
limpa = '\033[m'

n1 = int(input('Digite um número: {}'.format(textpurple)))
ant = n1 - 1
suc = n1 + 1
print('{}Número {}{}{}'.format(limpa,textpurple,n1,limpa))
print('Antecessor {}{}{}'.format(textred,ant,limpa))
print('Sucessor {}{}{}'.format(textgreen,suc,limpa))