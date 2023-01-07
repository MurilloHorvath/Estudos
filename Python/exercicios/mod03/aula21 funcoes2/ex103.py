
def ficha(nome='<desconhecido>',gols='0'):
    print('-'*20)
    print(f'O jogador {nome} fez {gols} Gol(s) no campeonato')


nome = str(input('Digite o nome do jogador: ')).strip()
gols = str(input('Digite quantos gols ele fez em cada partida: '))
if nome=='' and gols=='':
    ficha()
elif nome=='':
    ficha(gols=gols)
elif gols=='':
    ficha(nome)
else:
    ficha(nome,gols)