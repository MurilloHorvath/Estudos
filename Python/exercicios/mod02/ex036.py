import time
textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

vcasa = float(input('Qual é o valor da casa? {}'.format(textgreen)))
sal = float(input('{}Qual é o salario do comprador? {}R$'.format(limpa,textgreen)))
anos = float(input('{}Quantos anos para pagar? {}'.format(limpa,textgreen)))

prestacao = vcasa / (anos * 12)
porcent = sal * 0.3
print('{}Analisando...'.format(limpa))
time.sleep(1)

if porcent>prestacao:
    print('O comprador esta {}APTO{} para fazer o emprestimo!'.format(textgreen,limpa))
    print('Obrigado pela preferencia, tenha um bom dia.')
else:
    print('O comprador {}NÂO{} pode fazer o emprestimo...'.format(textred,limpa))
    print('Nós lamentamos, tenha um bom dia.')

print(porcent)
print(round(prestacao,2))