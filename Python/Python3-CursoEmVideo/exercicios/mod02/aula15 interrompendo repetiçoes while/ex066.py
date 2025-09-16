tot = quant = 0
while True:
    num = int(input('Digite um Número: '))
    if num == 999:
        break
    tot+=num 
    quant+=1
media = tot / quant
print(f'De {quant} Números digitados o Total é {tot}')
print(f'A Média entre eles é {media}')