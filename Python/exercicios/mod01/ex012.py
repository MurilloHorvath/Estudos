textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

produto = float(input('Digite o preço do produto: {}'.format(textgreen)))
porcentagem = float(input('{}Digite a porcentagem de desconto: {}'.format(limpa,textred)))
desconto = porcentagem / 100
despreço = produto - (desconto * produto)
print('{}O preço do produto agora apos o desconto é {}R${:.2f}{}'.format(limpa,textyellow,despreço,limpa))