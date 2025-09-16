textred = '\033[31m'
textblue = '\033[36m'
limpa = '\033[m'

n = str(input('Digite seu Nome: {}'.format(textred))).strip()

nome = n.split()

print('{}Primero Nome: {}{}{}'.format(limpa,textred,nome[0],limpa))
print('Ultimo Nome: {}{}{}'.format(textblue,nome[len(nome) - 1],limpa))
