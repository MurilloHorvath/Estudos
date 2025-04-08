from time import sleep
def maior(num):
    maiorn = 0
    print('Analisando valores informados')
    for n in num:
        print(f'{n} ',end='',flush=True)
        sleep(0.2)
        if n>maiorn:
            maiorn = n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'De todos os valores o maior é {maiorn}')


lista = list()
while True:
    numero = int(input('Digite um numero intero: '))
    lista.append(numero)
    cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'nN':
        break

maior(lista)