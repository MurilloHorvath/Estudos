matriz = [[],[],[]]
spar=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}] ',end='')
        if matriz[l][c] % 2 == 0:
            spar+=matriz[l][c]
        if c == 2:
            scol+=matriz[l][c]
    if l == 1:
        maiv = max(matriz[l])
    print()
print('-='*20)
print(f'A soma de todos os valores Pares: {spar}')
print(f'A soma de todos os valores da terceira coluna : {scol}')
print(f'O maior valor da segunda linha: {maiv}')
