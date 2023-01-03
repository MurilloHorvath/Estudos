matriz = list()
valores = list()
pares = 0
coluna3 = 0
maiv = 0
for c in range(0,3):
    valores.clear()
    for l in range(0,3):
        valores.append(int(input(f'Digite um valor para [{c}, {l}]: ')))
    matriz.append(valores[:])

print(f'''
[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]
[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]
[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]
''')

for l,col in enumerate(matriz):
    for c,v in enumerate(col):
        if v%2==0:
            pares+=v
        if c==2:
            coluna3+=v
    if l == 1:
        maiv = max(col)

print(f'A soma de todos os valores Pares: {pares}')
print(f'A soma de todos os valores da terceira coluna : {coluna3}')
print(f'O maior valor da segunda linha: {maiv}')

