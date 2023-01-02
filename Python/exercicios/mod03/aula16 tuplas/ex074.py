import random 

num = (random.randint(0,100),random.randint(0,100),
random.randint(0,100),random.randint(0,100),
random.randint(0,100))

print('Os valores sorteados foram: ', end='')
for n in num:
    print(n, end=' ')

print(f'\nO menor valor sorteado foi {min(num)}')
print(sorted(num)[0])
print(f'O maior valor sorteador foi {max(num)}')
print(sorted(num)[4])
