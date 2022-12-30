a = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
res = a
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(' {} ->'.format(res),end='')
        res+=r
        c+=1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
