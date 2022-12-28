import time


num = int(input('Digite um número inteiro: '))
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
base = int(input('Escolha qual sera a base da conversão: '))

if base == 1:
    print('Modo escolhido - Binário')
    print('Fazendo conversão...')
    time.sleep(1)
    bin = bin(num)
    print('Conversão concluida: Inteiro {} -> Binário {}'.format(num,bin))
elif base == 2:
    print('Modo escolhido - Octal')
    print('Fazendo conversão...')
    time.sleep(1)
    oct = oct(num)
    print('Conversão concluida: Inteiro {} -> Octal {}'.format(num,oct))
elif base == 3:
    print('Modo escolhido - Hexadecimal')
    print('Fazendo conversão...')
    time.sleep(1)
    hex = hex(num)
    print('Conversão concluida: Inteiro {} -> Hexadecimal {}'.format(num,hex))
else:
    print('============ERRO============')
    print('Modo escolhido é inexistente')