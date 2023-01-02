lista = ('Lápis',1.75,
'Borracha',2,
'Caderno',15.90,
'Estojo',25,
'Transferidor',4.20,
'Compasso',9.99,
'Mochila',120.32,
'Canetas',22.30,
'Livro',34.90)
print('-'*30)
print(f'{"Listagem de Preços":^30}')
print('-'*30)
for c in range(0,len(lista),2):
    print(f'{lista[c]:.<20}R${lista[c+1]:>7.2f}')
print('-'*30)