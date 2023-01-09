def leiaInt(text):
    while True:
        try:
            n = int(input(f'{text}'))
        except Exception as erro:
            print(f'{cores("Vermelho")}{erro.__class__}! Opção Inválida!{cores("Limpa")}')
        except KeyboardInterrupt:
            print(f'{cores("Vermelho")}Entrada de dados interrompida pelo usuário.{cores("Limpa")}')
            return 0
        else:
            return n

def cores(cor):
    cores = {'Limpa':'\033[m',
            'Vermelho':'\033[31m',
            'Verde':'\033[32m',
            'Amarelo':'\033[33m',
            'Roxo':'\033[34m',
            'Roza':'\033[35m',
            'Azul':'\033[36m'
            }
    return cores[cor]

def linha(tam=42):
    return '-'*tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cores("Amarelo")}{c}{cores("Limpa")} - {cores("Azul")}{item}{cores("Limpa")}')
        c+=1
    print(linha())
    opc = leiaInt(f'{cores("Verde")}Sua Opção: {cores("Limpa")}')
    return opc