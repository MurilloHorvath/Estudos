pessoas = list()
dados = list()
maip = menp = 0
print('Cadastro de Nome e Peso')
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])

    if len(pessoas) == 0:
        maip = menp = dados[1]
    else:
        if dados[1] > maip:
            maip = dados[1]
        if dados[1] < menp:
            menp = dados[1]

    dados.clear()
    esc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while esc not in 'SsNn':
        print('Erro. Tente Novamente')
        esc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if esc in 'Nn':
        print('Finalizando cadastros..')
        break

print(f'O total de pessoas cadastradas foram: {len(pessoas)}')
print(f'O maior peso foi de {maip}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == maip:
        print(f'[{p[0]}] ',end='')
print(f'\nO menor peso foi de {menp}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == menp:
        print(f'[{p[0]}] ',end='')
        