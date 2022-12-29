a = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
c = 0
x = 0
t=0
while c != 1:
    res = a + x * r
    x+=1
    print(res,end='->')
    if x == 10 or x == t+10:
        print('\nVocê quer ver mais termos?')
        termos = int(input('Quantos?'))
        t+=termos
        if termos == 0:
            print('FIM')
            c+=1
