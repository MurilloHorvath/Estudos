limpa = '\033[m'
textred = '\033[31m'
textgreen = '\033[32m'
textpurple = '\033[34m'

n1 = int(input('Digite um valor: {}'.format(textred)))
n2 = int(input('{}Digite outro valor: {}'.format(limpa,textgreen)))
s = n1 + n2

print('{}A soma entre {}{}{} e {}{}{} é igual a {}{}{}'.format(limpa,textred,n1,limpa,textgreen,n2,limpa,textpurple,s,limpa))
