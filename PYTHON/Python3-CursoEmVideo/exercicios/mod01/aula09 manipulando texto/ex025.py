textgreen = '\033[32m'
limpa = '\033[m'

nome = str(input('Digite seu Nome: {}'.format(textgreen))).strip()

print('{}Você tem Silva no Nome? {}{}{}'.format(limpa,textgreen,'SILVA' in nome.upper(),limpa))
