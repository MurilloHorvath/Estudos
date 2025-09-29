def leiaInt(text):
    while True:
        try:
            n = int(input(f'{text}'))
        except Exception as erro:
            print(f'\033[31m{erro.__class__}! número inteiro inválido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiaFloat(text):
    while True:
        try:
            n = float(input(f'{text}'))
        except Exception as erro:
            print(f'\033[31m{erro.__class__}! número real inválido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return n

n1 = leiaInt('Digite um Número inteiro: ')
print(f'Você acabou de digitar o número {n1}')
n2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {n2}')