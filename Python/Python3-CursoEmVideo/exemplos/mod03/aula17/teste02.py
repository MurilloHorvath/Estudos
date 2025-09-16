# podemos começar uma lista vazia assim..
# valores = list()
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}..',end='')
print('\n')

for c,v in enumerate(valores):
    print(f'na posição {c} encontrei {v}!')
print('Cheguei ao final da lista.')