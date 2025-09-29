a = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
res = a
while c <= 10:
    print(res,end='->')
    res+=r
    c+=1
print('Fim')
