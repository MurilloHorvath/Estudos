def somar(a=0,b=0,c=0):
    """
    -> F az a soma de tres valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c:  o terceiro valor(opcional)
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(3,2)
somar(c=3,a=2)
somar()