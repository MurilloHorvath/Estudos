valor = float(input('Digite o valor do produto: R$'))
print('à vista Dinheiro/Cheque - 1')
print('á vista Cartão - 2')
print('Em até 2x no Cartão - 3')
print('3x ou mais no Cartão - 4')
form = int(input('Escolha uma das formas de pagamento: '))

if form == 1:
    print('Forma de pagamento selecionada: 1')
    total = valor * 0.9
    print('Total a pagar será R${:.2f}'.format(total))
elif form == 2:
    print('Forma de pagamento selecionada: 2')
    total = valor * 0.95
    print('Total a pagar será R${:.2f}'.format(total))
elif form == 3:
    print('Forma de pagamento selecionada: 3')
    print('Serão 2 parcelas de R${:.2f}'.format(valor/2))
    print('Total a pagar será R${:.2f}'.format(valor))
elif form == 4:
    print('Forma de pagamento selecionada: 4')
    parcelas = int(input('Quantas parcelas: '))
    total = valor * 1.2
    print('Serão {} parcelas de R${:.2f}'.format(parcelas,total/parcelas))
    print('Total a pagar será R${:.2f}'.format(total))
else:
    print('ERRO')
    