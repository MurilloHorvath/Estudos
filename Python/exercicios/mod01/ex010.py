textgreen = '\033[32m'
limpa = '\033[m'

reais = float(input('Quantos reais voce tem na carteira? {}'.format(textgreen)))
dolares = reais / 5.17
print('{}Fazendo a conversão voce possui {}{:.2f}{} dólares!'.format(limpa,textgreen,dolares,limpa))
