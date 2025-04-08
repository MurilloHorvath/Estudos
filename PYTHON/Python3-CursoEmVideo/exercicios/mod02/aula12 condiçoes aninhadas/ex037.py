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
    print('Conversão concluida: Inteiro {} -> Binário {}'.format(num,bin(num)[2:]))
elif base == 2:
    print('Modo escolhido - Octal')
    print('Fazendo conversão...')
    time.sleep(1)
    print('Conversão concluida: Inteiro {} -> Octal {}'.format(num,oct(num)[2:]))
elif base == 3:
    print('Modo escolhido - Hexadecimal')
    print('Fazendo conversão...')
    time.sleep(1)
    print('Conversão concluida: Inteiro {} -> Hexadecimal {}'.format(num,hex(num)[2:]))
else:
    print('============ERRO============')
    print('Modo escolhido é inexistente')