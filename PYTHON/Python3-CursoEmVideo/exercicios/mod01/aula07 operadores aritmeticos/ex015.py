textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

dias = int(input('Quantos dias alugados? {}'.format(textred)))
km = float(input('{}Quantos Km rodados? {}'.format(limpa,textred)))
valor = (60*dias) + (0.15*km)
print('{}O total a pagar é de {}R${:.2f}{}'.format(limpa,textgreen,valor,limpa))