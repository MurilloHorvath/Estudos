from random import randint

def sorteia():
    for n in range(0,5):
        numeros.append(randint(1,10))
    print(f'Os numeros sorteados foram: {numeros}')
def somaPar(list):
    for v in list:
        if v%2==0:
            cont+=v
    print(f'A soma entre eles é {cont}')

numeros = list()
cont=0
sorteia()
somaPar(numeros)

