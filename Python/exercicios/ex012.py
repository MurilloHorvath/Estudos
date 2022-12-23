produto = float(input('Digite o preço do produto: '))
porcentagem = float(input('Digite a porcentagem de desconto: '))
desconto = porcentagem / 100
despreço = produto - (desconto * produto)
print('O preço do produto agora apos o desconto é R${:.2f}'.format(despreço))