
def teste(text):
    comando = f" Acessando o manual do comando '{text}' "
    print('\33[46m-\33[m'*len(comando))
    print(f'\33[46m{comando}\33[m')
    print('\33[46m-\33[m'*len(comando))
    help(text)


while True:
    print('\33[43m-\33[m'*25)
    print('\33[43m Sistema de ajuda PyHelp \33[m')
    print('\33[43m-\33[m'*25)
    func = str(input('Função ou Biblioteca > '))
    teste(func)
    cont = str(input('Deseja continuar?'))
    if cont in 'Nn':
        break