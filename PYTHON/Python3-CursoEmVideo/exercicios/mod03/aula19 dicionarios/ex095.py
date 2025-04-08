jogadores = list()
dados = dict()
gols = list()
while True:
    print('-'*40)
    dados['Nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for p in range(0,partidas):
        gols.append(int(input(f'Quantos Gols na partida {p+1}: ')))
    dados['Gols']=gols[:]
    dados['Total']=sum(gols)
    gols.clear()
    jogadores.append(dados.copy())
    cont = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'NS':
        cont = str(input('Deseja Continuar: [S/N] ')).strip().upper()[0]
    if cont in 'N':
        break
print('-='*40)
print(f'{"cod":<3} {"nomes":<15}{"gols":<15}{"total":<5}')
print('-'*40)
for k,v in enumerate(jogadores):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)
while True:
    esc = int(input('Mostrar dados de qual jogador? '))
    while esc<0 or esc>len(jogadores)-1 and esc != 999:
        print(f'ERRO! Não existe jogador com o codigo {esc} Tente novamente')
        print('-'*40)
        esc = int(input('Mostrar dados de qual jogador? '))
    if esc == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[esc]["Nome"]}:')
    for i,g in enumerate(jogadores[esc]['Gols']):
        print(f'    No jogo {i+1} fez {g} Gols')
    print('-'*40)
print('Encerrado')