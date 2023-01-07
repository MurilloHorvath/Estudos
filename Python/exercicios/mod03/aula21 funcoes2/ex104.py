
def leiaint(text):
    n = input(f'{text}')
    while n.isnumeric() == False:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        n = input(f'{text}')
    return n

n = leiaint('Digite um Número inteiro: ')
print(f'Você acabou de digitar o número {n}')