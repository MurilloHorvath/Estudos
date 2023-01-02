'''
num = ()
numpar = ()
for c in range(0,4):
    num1 = int(input('Digite um valor: '))
    num = num + (num1,)
    if num1%2 == 0:
        numpar = numpar + (num1,)
print(num)
print('Quantas vezes apareceram o número 9: ',num.count(9))
if num.count(3) == 0:
    print('O número 3 Não foi digitado em nenhuma posição')
else:
    print('Em qual posição está  o número 3: ',num.index(3))

print('Estes foram o números pares: ', numpar)
'''
num = (int(input('Digite um Número: ')),
int(input('Digite outro Número: ')),
int(input('Digite mais um Número: ')),
int(input('Digite o último Número: ')))
print(f'Você digitou os valores{num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 ==0:
        print(n,end=' ')
        