ano = int(input('Digite um ano: '))

if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print('{} Ano Bissexto'.format(ano))
        else:
            print('{} Ano Não Bissexto'.format(ano))
    else:
        print('{} Ano Bissexto'.format(ano))
else:
    print('{} Ano Não Bissexto'.format(ano))