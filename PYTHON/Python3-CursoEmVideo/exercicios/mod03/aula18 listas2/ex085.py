lista = [[],[]]
for n in range(1,8):
    num = int(input(f'Digite o {n}° valor: '))
    if num%2==0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()
print(f'Todos os valores: {lista}')
print(f'Valores Pares: {lista[0]}')
print(f'Valores Impares: {lista[1]}')
