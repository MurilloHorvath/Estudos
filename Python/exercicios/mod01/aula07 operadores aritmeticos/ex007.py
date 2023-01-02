textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

nota1 = float(input('Digite a primeira nota do aluno: {}'.format(textred)))
nota2 = float(input('{}Digite a segunda nota do aluno: {}'.format(limpa,textred)))
media = (nota1 + nota2) / 2
print('{}A média da nota do aluno é {}{}{}'.format(limpa,textgreen,media,limpa))
