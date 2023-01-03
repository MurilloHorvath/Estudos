matriz = list()
valores = list()
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
