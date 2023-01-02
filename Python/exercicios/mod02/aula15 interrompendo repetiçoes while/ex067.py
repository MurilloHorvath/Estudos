while True:
    print('-'*30)
    num = int(input('Digite um Número: '))
    print('-'*30)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {c:2} = {c*num}')
print('Finalizado')
