lista = list()
listapar = list()
listaimpar = list()
print('Digite os valores que deseja adicionar a lista.')
while True:
    lista.append(int(input('Digite o valor: ')))
    cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while cont not in 'SN':
        print('Tente Novamente.')
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont in 'N':
        print('Analisando Valores da Lista..')
        break 

for v in lista:
    if v%2==0:
        listapar.append(v)
    else:
        listaimpar.append(v)

print(f'Lista: {lista}')
print(f'Lista dos valores pares: {listapar}')
print(f'Lista do valores impares: {listaimpar}')