valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    esc = str(input('Quer continuar? [S/N] ')).upper()
    while esc not in 'sSnN':
        esc = str(input('Tente novamente.Quer continuar? [S/N]')).upper()
    if esc in 'Nn':
        print('Finalizando programa..')
        break
print('-='*20)
valores.sort()
print(f'Você digitou os valores {valores}')