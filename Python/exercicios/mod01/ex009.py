textgreen = '\033[32m'
limpa = '\033[m'

n1 = int(input('Digite um número inteiro: {}'.format(textgreen)))
print('-'*12)
print('{}{} x  1 = {}{}{}'.format(limpa,n1,textgreen,n1*1,limpa))
print('{} x  2 = {}{}{}'.format(n1,textgreen,n1*2,limpa))
print('{} x  3 = {}{}{}'.format(n1,textgreen,n1*3,limpa))
print('{} x  4 = {}{}{}'.format(n1,textgreen,n1*4,limpa))
print('{} x  5 = {}{}{}'.format(n1,textgreen,n1*5,limpa))
print('{} x  6 = {}{}{}'.format(n1,textgreen,n1*6,limpa))
print('{} x  7 = {}{}{}'.format(n1,textgreen,n1*7,limpa))
print('{} x  8 = {}{}{}'.format(n1,textgreen,n1*8,limpa))
print('{} x  9 = {}{}{}'.format(n1,textgreen,n1*9,limpa))
print('{} x 10 = {}{}'.format(n1,textgreen,n1*10))
print('-'*12,'\033[m')

