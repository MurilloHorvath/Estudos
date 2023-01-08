def voto(nasc):
    from datetime import date
    a = date.today().year - nasc
    if a<16:
        return f'Com {a} anos: VOTO NEGADO'
    elif 16<=a<18 or a>=65:
        return f'Com {a} anos: VOTO OPCIONAL'
    else:
        return f'Com {a} anos: VOTO OBRIGATÓRIO'

    
data = int(input('Insira o seu ano de nascimento: '))
print(voto(data))
