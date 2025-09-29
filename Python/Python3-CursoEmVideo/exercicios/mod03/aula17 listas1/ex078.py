num = list()

for cont in range(0,5):
    num.append(int(input('Digite um valor: ')))
print('=-='*10)
print(num)
print(f'O maior valor encontrado foi {max(num)} e suas posições são ',end='')
for p,v in enumerate(num):
    if v == max(num):
        print(f'{p}..',end=' ')
print(f'\nO menor valor encontrado foi {min(num)} e suas posições são ',end='')
for p,v in enumerate(num):
    if v == min(num):
        print(f'{p}..',end=' ')
print('\nFIM!')