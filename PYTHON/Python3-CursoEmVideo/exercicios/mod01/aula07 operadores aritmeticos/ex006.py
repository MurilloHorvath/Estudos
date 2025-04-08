limpa = '\033[m'
textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
textpurple = '\033[34m'
textpink = '\033[35m'

n1 = int(input('Digite um número: {}'.format(textred)))
dob = n1*2
tri = n1*3
raiz = n1**(1/2)
print('{}Número {}{}{}'.format(limpa,textgreen,n1,limpa))
print('Dobro {}{}{}'.format(textyellow,dob,limpa))
print('Triplo {}{}{}'.format(textpurple,tri,limpa))
print('Raiz quadrada {}{:.2f}{}'.format(textpink,raiz,limpa))
