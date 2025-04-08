total = 0
mais_velho = 0
nome_mais_velho = ''
menos_de_vinte = 0

for x in range(1,5):
    print('==== {}° Pessoa ===='.format(x))
    nome = str(input('Digite o Nome: ')).strip()
    idade = int(input('Digite a Idade: '))
    sexo = int(input('0-Masc  1-Fem  '))
    total += idade
    media = total / 4
    if idade > mais_velho and sexo == 0:
        nome_mais_velho = nome 
        mais_velho = idade
    if idade < 20 and sexo == 1:
        menos_de_vinte+=1

print('A média de idade do grupo é {:.1f} Anos'.format(media))
print('O nome do homem mais velho é {}'.format(nome_mais_velho))
print('Ha no total {} Mulheres mais novas do que 20 anos'.format(menos_de_vinte))