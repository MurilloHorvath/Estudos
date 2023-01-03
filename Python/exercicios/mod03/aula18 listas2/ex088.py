from random import randint

lista = list()
dados = list()
jogos = int(input('Quantos jogos você quer gerar? '))

for j in range(0,jogos):
    dados.clear()
    for n in range(0,6):
        dados.append(randint(1,60))
    lista.append(dados[:])

print(lista)