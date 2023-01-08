from time import sleep
c = ('\033[m',        # 0 - SEM CORES
     '\033[0;30;41m', # 1 - VERMELHO
     '\033[0;30;42m', # 2 - VERDE 
     '\033[0;30;43m', # 3 - AMARELO
     ) 

def teste(text):
    titulo(f'Acessando o manual do comando \'{text}\'',2)
    print(c[3],end='')
    help(text)
    print(c[0],end='')
    sleep(2)

def titulo(msg,cor=0):
    tam = len(msg)+4
    print(c[cor],end='')
    print('-'*tam)
    print(f'  {msg}  ')
    print('-'*tam)
    print(c[0],end='')
    sleep(1)

func = ''
while True:
    titulo('Sistema de ajuda PyHelp', 1)
    func = str(input('Função ou Biblioteca > '))
    if func.upper() in 'FIM':
        break
    else:
        teste(func)

titulo('ATÉ LOGO', 1)