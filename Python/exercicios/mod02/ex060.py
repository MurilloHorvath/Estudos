num = int(input('Digite um número: '))
c = 0
fac = num - 1
res = num
while c != 1:
    res = res * fac
    fac-=1
    if fac == 1:
        print('O fatorial de {} é {}'.format(num,res))
        print('fim')
        c+=1
