print('Digite os valores a baixo: ')
s = 0
for c in range(1,7):
    num = int(input(' '))
    if num%2 == 0:
        s += num
print('A soma dos valores pares é {}'.format(s))