dist = int(input('Qual a distância da viagem?'))

if dist>200:
    print('Viagem Longa...')
    preço = dist * 0.45
    print('Total a pagar R${:.2f}'.format(preço))
else:
    print('Viagem normal...')
    preço = dist * 0.50
    print('Total a pagar R${:.2f}'.format(preço))
print('Boa Viagem!')