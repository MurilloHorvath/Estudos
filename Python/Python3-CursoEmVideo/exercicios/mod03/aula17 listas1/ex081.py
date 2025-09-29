lista = list()
while True:
    lista.append(int(input('Digite o valor que deseja adicionar a lista: ')))
    fim = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while fim not in 'SN':
        fim = str(input('Tente Novamente.\nDeseja continuar? [S/N]')).upper()
    if fim in 'N':
        print('Analisando dados da lista..')
        break

print(f'Foram encontrados {len(lista)} Números na lista.')
lista.sort(reverse=True)
print(f'Esses Números são {lista}')
if 5 in lista:
    print('O Número 5 está na lista!')
else:
    print('O Número 5 não está na lista..')