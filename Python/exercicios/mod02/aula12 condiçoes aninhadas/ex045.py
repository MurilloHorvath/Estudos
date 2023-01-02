import random
import time

esc = int(input('Pedra - 0 , Papel - 1 , Tesoura - 2 ...'))
escpc = random.randint(0,2)

jokenpo = ('Pedra','Papel','Tesoura')

print('JO..')
time.sleep(0.5)
print('KEN..')
time.sleep(0.5)
print('Pô!')

print('-='*10)
print('O jogador jogou {}'.format(jokenpo[esc]))
print('O computador jogou {}'.format(jokenpo[escpc]))
print('-='*10)

if esc == 0:
    if escpc == 1:
        print('Perdeu!')
    elif escpc == 2:
        print('Ganhou!')
    else:
        print('Empate..')
elif esc == 1:
    if escpc == 0:
        print('Ganhou!')
    elif escpc == 2:
        print('Perdeu!')
    else:
        print('Empate..')
elif esc == 2:
    if escpc == 0:
        print('Perdeu!')
    elif escpc == 1:
        print('Ganhou!')
    else:
        print('Empate..')
else:
    print('ERRO')
