math = str(input('Escreva uma expressão: '))
teste = list()
for c in math:
    if c in '(':
        teste.append(c)
    elif c in ')':
        if len(teste)>0:
            teste.pop()
        else:
            teste.append(c)
            break
if len(teste)==0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')