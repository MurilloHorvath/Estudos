textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

salario = float(input('Digite o salário do funcionário: {}'.format(textgreen)))
porcentagem = int(input('{}Digite quanto de aumento em porcentagem o funcionário vai receber: {}'.format(limpa,textred)))
aumento = porcentagem / 100
atual = salario + (aumento*salario)
var = "%"
print('{}O salário do funcionario era {}R${:.2f}{} agora após o aumento de {}{}{}{} ele vai receber {}R${:.2f}{}'.format(limpa,textred,salario,limpa,textred,porcentagem,var,limpa,textgreen,atual,limpa))