soma = quant = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant+=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e media entre eles é {}'.format(quant,media))
print('De todos os numeros o Maior é {} e o Menor é {}'.format(maior,menor))
