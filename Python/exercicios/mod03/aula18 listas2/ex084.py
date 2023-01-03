pessoas = list()
dados = list()
nommai = list()
nommen = list()
maip = menp = 0
print('Cadastro de Nome e Peso')
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if maip == 0 or menp == 0:
        maip = dados[1]
        nommai.append(dados[0])
        menp = dados[1]
        nommen.append(dados[0])
    elif dados[1] >= maip:
        if dados[1] != maip:
            maip = dados[1]
            nommai.clear()
            nommai.append(dados[0])
        else:
            maip = dados[1]
            nommai.append(dados[0])
    elif dados[1] <= menp:
        if dados[1] != menp:
            menp = dados[1]
            nommen.clear()
            nommen.append(dados[0])
        else:
            menp = dados[1]
            nommen.append(dados[0])
    dados.clear()
    esc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while esc not in 'SsNn':
        print('Erro. Tente Novamente')
        esc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if esc in 'Nn':
        print('Finalizando cadastros..')
        break

print(f'O total de pessoas cadastradas foram: {len(pessoas)}')
print(f'O maior peso foi de {maip}Kg. Peso de {nommai}')
print(f'O menor peso foi de {menp}Kg. Peso de {nommen}')
