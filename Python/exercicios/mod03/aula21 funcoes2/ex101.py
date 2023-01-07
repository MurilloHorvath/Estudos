from datetime import date

def voto(nasc):
    a = date.today().year - nasc
    if 70>a>=18:
        print(f'Com {a} anos: VOTO OBRIGATÓRIO')
    elif a>=70 or a>=16:
        print(f'Com {a} anos: VOTO OPCIONAL')
    else:
        print(f'Com {a} anos: VOTO NEGADO')

    

data = int(input('Insira o seu ano de nascimento: '))
voto(data)