a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))

if a+b > c and a+c > b and b+c > a:
    print('Pode ser um triangulo')
else:
    print('Não pode ser um triangulo')