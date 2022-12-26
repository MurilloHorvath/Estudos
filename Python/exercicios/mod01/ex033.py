n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print('{} Este é o maior número'.format(n1))
else:
    if n2 > n3:
        print('{} Este é o maior número'.format(n2))
    else:
        print('{} Este é o maior número'.format(n3))
