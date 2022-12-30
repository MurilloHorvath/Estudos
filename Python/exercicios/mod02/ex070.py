totcompra = milmais = maisbarato = 0
nomebarato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))

    totcompra+=preco
    if preco>1000:
        milmais+=1
    if maisbarato == 0 or preco<maisbarato:
        nomebarato = nome
        maisbarato = preco

    parar = ' '
    while parar not in 'SN':
        parar = str(input('Você quer continuar? [S/N]')).strip().upper()[0]

    if parar in 'N':
        break

print('Compra finalizada..')
print(f'O total da compra deu {totcompra:.2f}')
print(f'Temos {milmais} Custando mais de R$1000')
print(f'O produto mais barato foi {nomebarato} que custa R${maisbarato:.2f}')
