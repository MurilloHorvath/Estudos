
def notas(*n):
    maior=menor=media=tot=0
    boletim = dict()
    for c in n:
        if maior == 0 and menor == 0:
            maior = menor = c
        if c>maior:
            maior=c
        elif c<menor:
            menor=c
        tot+=c
    media=tot/len(n)
    boletim['Quantidade de Notas'] = len(n)
    boletim['Maior Nota'] = maior
    boletim['Menor Nota'] = menor
    boletim['Média'] = media
    if media>=7:
        boletim['Situação'] = 'Excelente'
    elif media>4:
        boletim['Situação'] = 'Boa'
    else:
        boletim['Situação'] = 'Ruim'
    return boletim
resp = notas(5.6,7,8,7.5)
print(resp)