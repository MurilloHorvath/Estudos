from random import shuffle

textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

a1 = str(input('Primeiro aluno: {}'.format(textred)))
a2 = str(input('{}Segundo aluno: {}'.format(limpa,textred)))
a3 = str(input('{}Terceiro aluno: {}'.format(limpa,textred)))
a4 = str(input('{}Quarto aluno: {}'.format(limpa,textred)))

lista = [a1, a2, a3, a4]
shuffle(lista)

print('{}{}A ordem de apresentação será{}'.format(limpa,textgreen,limpa))
print(textgreen)
print(lista)
print(limpa)