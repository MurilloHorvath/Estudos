from time import sleep
def contador(i,f,p):
    if p == 0:
        p = 1
    # elif p < 0:
        
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if f<i:
        for n in range(f,i+1,p):
            print(f'{n}-> ',end='')
        print('FIM!')
    else:
        for n in range(i,f+1,p):
            print(f'{n}-> ',end='')
        print('FIM!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)