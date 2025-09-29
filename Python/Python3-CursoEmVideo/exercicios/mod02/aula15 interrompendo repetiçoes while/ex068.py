from random import randint
vitorias = 0
while True:
    pc = randint(1,5)
    op = str(input('Par ou impar? [P/I]')).strip().upper()
    while op not in 'PI':
        op = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    player = int(input('3 .. 2 .. 1..'))
    tot = player + pc
    print(f'Você jogou {player} e o pc jogou {pc}.. Total {tot} ', end='')
    print('DEU PAR' if tot%2==0 else 'DEU IMPAR')
    if op == 'P' and tot%2==0:
        print('Venceu!')
        vitorias+=1
    elif op == 'I' and tot%2==1:
        print('Venceu!')
        vitorias+=1
    else:
        print('Perdeu..')
        break
print(f'{vitorias} Vitorias consecutivas')
