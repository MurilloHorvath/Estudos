nome = str(input('Digite seu Nome completo: ')).strip()

print('Todas Maiúsculas:',nome.upper())
print('Todas Minúsculas:',nome.lower())
print('Quantas letras tem o Nome:',len(nome) - nome.count(' '))
#print('Quantas letras tem o primeiro Nome:',nome.find(' '))
splitnome = nome.split
print('Quantas letras tem seu primeiro nome:', len(splitnome[0]))
