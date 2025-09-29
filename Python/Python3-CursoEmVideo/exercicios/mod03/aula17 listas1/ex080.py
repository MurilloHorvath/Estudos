valores = list()
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if len(valores) == 0 or num >= max(valores):   
        print('Adicionando ao final da lista.')
        valores.append(num)
    else:
        for p,v in enumerate(valores):
            if v>num:
                print(f'Adicionando na posição {p} da lista')
                valores.insert(p,num)
                break
print('-='*20)
print('Os valores digitados em ordem foram ',valores)
