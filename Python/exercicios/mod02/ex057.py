'''
c = 0
while c != 1:
    r = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
    if r == 'M':
        c+=1
    if r == 'F':
        c+=1
print('Fim')
'''
sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} Registrado'.format(sexo))
