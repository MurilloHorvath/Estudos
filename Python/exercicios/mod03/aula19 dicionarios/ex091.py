from random import randint

jogadores = dict()

for jogador in range(1,5):
    jogadores[f'jogador {jogador}'] = randint(1,6)

print(jogadores)
maior = 0
for a,b in jogadores.items():
    if b>maior:
        maior=b
        vencedor=a

print(f'O Vencedor foi o {vencedor} tirando {maior} no dado!')