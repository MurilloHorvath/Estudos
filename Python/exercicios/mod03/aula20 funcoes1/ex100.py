from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores:')
    print(f'Os numeros sorteados foram: ',end='')
    for n in range(0,5):
        v = randint(1,10)
        print(f'{v} ',end='',flush=True)
        sleep(0.3)
        lista.append(v)
    print('Pronto!')

def somaPar(lista):
    cont=0
    for v in lista:
        if v%2==0:
            cont+=v
    print(f'A soma entre os números pares é {cont}')

numeros = list()
sorteia(numeros)
somaPar(numeros)

