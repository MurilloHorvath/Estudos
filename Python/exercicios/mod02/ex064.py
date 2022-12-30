num = tot = quant = 0
num = int(input('Digite um numero inteiro: '))
while num != 999:
    tot+=num
    quant+=1
    num = int(input('Digite um numero inteiro: '))

print('No total foram {} Números digitados'.format(quant))
print('Somando todos eles temos o resultado de {}'.format(tot))