from random import randint
import time
lista = list()
dados = list()
jogos = int(input('Quantos jogos você quer gerar? '))
for j in range(0,jogos):
    for n in range(0,16):
        num = randint(1,25)
        while num in dados:
            num = randint(1,25)
        dados.append(num)
    lista.append(dados[:])
    dados.clear()

print(f'-=-= Sorteando {len(lista)} Jogos =-=-')
for j in range(0,len(lista)):
    lista[j].sort()
    print(f'Jogo {j+1}: {lista[j]}')
    time.sleep(1)