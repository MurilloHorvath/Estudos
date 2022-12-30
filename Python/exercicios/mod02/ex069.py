tot18 = masc = fem = 0
while True:
    print('-'*15)
    print('Cadastro:')
    print('-'*15)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18+=1
    if sexo in 'Mm':
        masc+=1
    if sexo in 'Ff' and idade<20:
        fem+=1
    print('-'*15)
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Você quer continuar? [S/N]')).strip().upper()
    if parar in 'Nn':
        break
print('Cadastros: ')
print(f'Usuários com Mais de 18 anos : {tot18}')
print(f'Usuários Masculinos: {masc}')
print(f'Usuários Femininos com menos de 20 anos: {fem}')
