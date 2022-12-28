textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))

media = (n1 + n2) / 2

if media<5.0:
    print('{}REPROVADO{}'.format(textred,limpa))
elif 5.0<=media>=6.9:
    print('{}RECUPERAÇÃO{}'.format(textyellow,limpa))
else:
    print('{}APROVADO{}'.format(textgreen,limpa))
    