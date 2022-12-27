textgreen = '\033[32m'
textyellow = '\033[33m'
textpurple = '\033[34m'
textpink = '\033[35m'
textblue = '\033[36m'
limpa = '\033[m'

n = int(input('Digite um número de 0 a 9999: {}'.format(textgreen)))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('{}Analisando o número {}{}{}'.format(limpa,textgreen,n,limpa))
print('Unidade: {}{}{}'.format(textyellow,u,limpa))
print('Dezena: {}{}{}'.format(textpurple,d,limpa))
print('Centena: {}{}{}'.format(textpink,c,limpa))
print('Milhar: {}{}{}'.format(textblue,m,limpa))
