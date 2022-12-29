mapeso = 0
mepeso = 0

for x in range(1,6):
    p = float(input('Digite o peso da {}° Pessoa: '.format(x)))
    if x == 1:
        maior = p
        mepeso = p 
    else:
        if p > maior:
            maior = p 
            map = x 
        if p < menor:
            menor = p 
            mep = x

print('Das 5 Pessoas a {}° é a mais pesada.. pesando {}Kg'.format(map,maior))
print('Das 5 Pessoas a {}° é a mais leve.. Pesando {}Kg'.format(mep,menor))
