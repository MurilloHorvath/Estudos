from random import choice

textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

a1 = str(input('Primeiro aluno: {}'.format(textred)))
a2 = str(input('{}Segundo aluno: {}'.format(limpa,textred)))
a3 = str(input('{}Terceiro aluno: {}'.format(limpa,textred)))
a4 = str(input('{}Quarto aluno: {}'.format(limpa,textred)))

lista = [a1,a2,a3,a4]

escolhido = choice(lista)

print('{}O aluno escolhido foi {}{}{}'.format(limpa,textgreen,escolhido,limpa))