from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
print('Valores sorteados:')
for jogador in range(1,5):
    jogadores[f'jogador {jogador}'] = randint(1,6)
    print(f'    O jogador {jogador} tirou {jogadores[f"jogador {jogador}"]} no dado!')
    sleep(0.5)
print('-'*20)
print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'    {i+1}° Lugar: {v[0]} com {v[1]}')
    sleep(0.5)