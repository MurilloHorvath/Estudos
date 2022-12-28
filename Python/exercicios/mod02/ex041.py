from datetime import date

nasc = int(input('Informe o ano de nascimento do atleta: '))

ano = date.today().year
idade = ano - nasc 

if idade<=9:
    print('MIRIM')
elif idade<=14:
    print('INFATIL')
elif idade<=19:
    print('JUNIOR')
elif idade<=20:
    print('SÊNIOR')
else:
    print('MASTER')