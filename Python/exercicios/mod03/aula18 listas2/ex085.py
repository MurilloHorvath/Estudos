pares = list()
impares = list()
lista = [pares,impares]

for n in range(1,8):
    num = int(input(f'Digite o {n}° valor: '))
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()
print(lista)