import random
print('O pc vai pensar em um número de 1 - 10 duvido voce acertar!')
acertou = False
palpites = 0
num = random.randint(0,10)
while not acertou:
    player = int(input('Digite seu palpite: '))
    palpites+=1
    if player == num:
        acertou = True
    else:
        if player < num:
            print('Você errou! - Mais')
        elif player > num:
            print('Você errou - Menos')

print('Depois de {} palpites Você Finalmente acertou!'.format(palpites))
print('O certo era {} desde o começo!'.format(num))
