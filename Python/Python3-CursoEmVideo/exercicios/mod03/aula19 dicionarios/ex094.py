pessoa = dict()
lista = list()
listMI = list()
totidade = 0
while True:
    pessoa['Nome'] = str(input('Digite o Nome: '))
    sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Tente Novamente. Digite o Sexo [M/F]: ')).strip().upper()[0]
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input('Digite a Idade: '))
    totidade+=pessoa['Idade']
    lista.append(pessoa.copy())
    cont = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Tente Novamente.Deseja Continuar? [S/N]')).strip().upper()[0]
    if cont in 'N':
        print('Finalizando..')
        break
print('-'*50)
print(f'- O grupo tem no total {len(lista)} Pessoas.')
print(f'- A média de idade do grupo é {totidade/len(lista):.0f} Anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for n in lista:
    if n['Sexo'] in 'F':
        print(f'{n["Nome"]} ',end='')
print(f'\n- Lista das Pessoas que estão com a idade acima da média:')
print()
for p in lista:
    if p['Idade']>=totidade/len(lista):
        print(f'Nome = {p["Nome"]}; Sexo = {p["Sexo"]}; Idade = {p["Idade"]};')
        print()
print('<<ENCERRADO>>')