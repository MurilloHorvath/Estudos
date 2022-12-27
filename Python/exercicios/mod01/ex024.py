textgreen = '\033[32m'
limpa = '\033[m'

cidade = str(input('Digite o nome de uma cidade: {}'.format(textgreen))).strip()
print('{}O nome da cidade começa com Santo? {}{}{}'.format(limpa,textgreen,cidade[:5].upper() == 'SANTO',limpa))