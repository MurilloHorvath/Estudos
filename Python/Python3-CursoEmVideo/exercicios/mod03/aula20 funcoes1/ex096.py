def area(l,c):
    res =  l*c 
    print(f'A area de um terreno {l}x{c} é de {res}m².')

print(' Controle de Terrenos')
print('-'*20)
larg = float(input('LARGURA: (m) '))
compr = float(input('COMPRIMENTO: (m) '))
area(larg,compr)