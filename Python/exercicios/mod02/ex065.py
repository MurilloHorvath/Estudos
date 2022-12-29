c=0
x=0
tot=0
maior = 0
menor = 0
while c != 1:
    num = int(input('Valor intero: '))
    x+=1
    tot+=num
    media = tot / x
    if x == 1 or num>maior:
        maior = num
    if x == 1 or num<menor:
        menor = num
    if x%5==0:
        print('A media entre os valores digitados é {}'.format(media))
        print('O maior valor lido foi {} e o menor valor lido foi {}'.format(maior,menor))
        op=str(input('Você deseja continuar inserindo valores? [S/N]')).strip().upper()
        if op == 'N':
            print('Finalizando Operação')
            c+=1
        elif op == 'S':
            continue
        else:
            print('ERRO - Interrompendo Operação')
            break
print('FIM')