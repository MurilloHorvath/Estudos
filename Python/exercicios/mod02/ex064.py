c = 0
tot=0
quant=0
while c != 1:
    num = int(input('Digite um numero inteiro: '))
    if num == 999:
        c+=1
    elif num != 999:
        quant+=1
        tot+=num

print('No total foram {} Números digitados'.format(quant))
print('Somando todos eles temos o resultado de {}'.format(tot))