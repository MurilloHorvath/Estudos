from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))

ano = date.today().year
idade = ano - nasc 

if idade < 18:
    print('Você ainda vai se alistar para o serviço militar')
    falta = 18 - idade
    print('Ainda falta {} anos para voce se alistar'.format(falta))
elif idade == 18:
    print('É a hora de você se alistar para o serviço militar')
elif idade > 18:
    print('Já possou da hora de você se alistar para o serviço militar')
    falta = idade - 18
    print('Passou {} anos de hora do seu alistamento'.format(falta))
else:
    print('===ERRO===')