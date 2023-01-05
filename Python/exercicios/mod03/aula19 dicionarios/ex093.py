dados = dict()
rend = list()
dados['Nome'] = str(input('Nome do Jogador: '))
dados['Partidas'] = int(input('Partidas Jogadas: '))
for g in range(0,dados['Partidas']):
    rend.append(int(input(f'Quantos gols na {g+1}° Partida: ')))
dados['Gols'] = rend
dados['Total de Gols'] = sum(rend)
print('-'*50)
print(dados)
print('-'*50)
for k,v in dados.items():
    print(f'{k}: {v}')
print('-'*50)
print(f'O jogador {dados["Nome"]} jogou {dados["Partidas"]} Partidas')
for p in range(0,dados['Partidas']):
    print(f'Na Partida {p+1}, fez {dados["Gols"][p]}.')
print(f'Foi um total de {dados["Total de Gols"]} Gols.')
