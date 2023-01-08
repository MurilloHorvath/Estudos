def ficha(nome,gols):
    if gols.isnumeric():
        g = int(gols)
    else:
        g=0
    print('-'*40)
    if nome=='':
        print(f'O jogador <desconhecido> fez {g} Gol(s) no campeonato')
    else:
        print(f'O jogador {nome} fez {g} Gol(s) no campeonato')


nome = str(input('Digite o nome do jogador: ')).strip()
gols = str(input('Digite quantos gols ele fez em cada partida: '))
ficha(nome,gols)