import random
escolha = int(input('Esacolha um número de 0 a 5: '))
num = random.randint(0,5)

if escolha == num:
    print('Você acertou!')
else:
    print('Você errou...')
    print('O certo era {}'.format(num))
