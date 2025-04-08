from time import sleep
def contador(i,f,p):
    if p == 0:
        p = 1
    elif p < 0:
        p*=-1
    print('-'*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if f<i:
        for n in range(f,i+1,p):
            print(f'{n} ',end='',flush=True)
            sleep(0.2)
        print('FIM!')
    else:
        for n in range(i,f+1,p):
            print(f'{n} ',end='',flush=True)
            sleep(0.2)
        print('FIM!')

contador(1,10,1)
contador(10,0,2)
print('-'*30)
print('Contagem Personalizada')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)