textgreen = '\033[32m'
textyellow = '\033[33m'
textpurple = '\033[34m'
textpink = '\033[35m'
limpa ='\033[m'

frase = str(input('Digite uma frase: {}'.format(textgreen))).upper().strip()

print('{}Quantas letras A tem na frase? {}{}{}'.format(limpa,textyellow,frase.count('A'),limpa))
print('Em qual posição ela aparece pela primeira vez? {}{}{}'.format(textpurple,frase.find('A') + 1,limpa))
print('Em qual posição ela aparece pela ultima vez? {}{}{}'.format(textpink,frase.rfind('A') + 1,limpa))
