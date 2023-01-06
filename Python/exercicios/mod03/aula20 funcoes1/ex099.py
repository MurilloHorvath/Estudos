def maior(num):
    maiorn = 0
    for n in num:
        if n>maiorn:
            maiorn = n
    print('Analisando valores informados')
    print(f'{num} foram informados {len(num)} valores ao todo.')
    print(f'De todos os valores o maior é {maiorn}')


lista = list()
while True:
    numero = int(input('Digite um numero intero: '))
    lista.append(numero)
    cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'nN':
        break

maior(lista)