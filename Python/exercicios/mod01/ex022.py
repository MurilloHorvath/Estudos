textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

nome = str(input('Digite seu Nome completo: {}'.format(textred))).strip()

print('{}Todas Maiúsculas: {}{}{}'.format(limpa,textyellow,nome.upper(),limpa))
print('Todas Minúsculas: {}{}{}'.format(textyellow,nome.lower(),limpa))
print('Quantas letras tem o Nome: {}{}{}'.format(textgreen,len(nome) - nome.count(' '),limpa))
print('Quantas letras tem o primeiro Nome: {}{}{}'.format(textgreen,nome.find(' '),limpa))
# splitnome = nome.split
# print('Quantas letras tem seu primeiro nome:', len(splitnome[0]))
