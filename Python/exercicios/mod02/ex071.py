print('Caixa Eletrônico')
valor = int(input('Quanto deseja sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total>=ced:
        total-=ced
        totced+=1

    else:
        if totced>0:
            print(f'Total de {totced} cédulas de R${ced}')

        if ced == 50:
            ced = 20
            totced = 0

        elif ced == 20:
            ced = 10
            totced = 0

        elif ced == 10:
            ced = 1
            totced = 0

        if total == 0:
            break
