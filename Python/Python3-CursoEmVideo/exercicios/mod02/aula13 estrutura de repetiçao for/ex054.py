from datetime import date
maior = 0
menor = 0
anoatual = date.today().year
for x in range(1,8):
    p = int(input('Digite o ano de nascimento da {}° Pessoa: '.format(x)))
    idade = anoatual - p
    if idade<18:
        menor+=1
    else:
        maior+=1
print('Das sete pessoas {} são maiores e {} são menores'.format(maior,menor))
