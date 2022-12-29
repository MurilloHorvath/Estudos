num = int(input('Digite um numero intero: '))
c = 0
x = 0
f1 = 0
f2 = 0
res=0
while c !=1:
    res = f1 + f2
    print(res,end='->')
    x+=1
    if f2 == 0:
        f2+=1
    if x%2==0:
        f2 = res
    if x%2==1:
        f1 = res
    if x == num:
        print('Fim')
        c+=1
