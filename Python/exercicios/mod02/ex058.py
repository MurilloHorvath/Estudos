import random
print('O pc vai pensar em um número de 1 - 10 duvido voce acertar!')
r = 0
palpites = 0
num = random.randint(0,10)
while r != 1:
    player = int(input('Digite seu palpite: '))
    palpites+=1
    if player == num:
        r+=1
    else:
        print('Você errou!')
print('Depois de {} palpites Você Finalmente acertou!'.format(palpites))
print('O certo era {} desde o começo!'.format(num))