a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))

if a < b+c and b < a+c and c < a+b:
    print('Pode formar um tringulo')
    print('Analisando o tipo de triangulo..')
    if a == b == c:
        print('Triângulo Equilátero')
    elif a == b or a == c or b == c:
        print('Triângulo Isósceles')
    elif a != b != c != a:
        print('Triângulo Escaleno')
else:
    print('Não pode formar um triângulo')
