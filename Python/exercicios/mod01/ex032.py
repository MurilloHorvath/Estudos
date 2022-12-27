textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

from datetime import date
ano = int(input('Digite um ano que deseja analisar: {}'.format(textyellow)))

if ano == 0:
    ano = date.today().year

if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('{}{} {}Ano Bissexto{}'.format(ano,limpa,textgreen,limpa))
        else:
            print('{}{} {}Ano Não Bissexto{}'.format(ano,limpa,textred,limpa))
    else:
        print('{}{} {}Ano Bissexto{}'.format(ano,limpa,textgreen,limpa))
else:
    print('{}{} {}Ano Não Bissexto{}'.format(ano,limpa,textred,limpa))
