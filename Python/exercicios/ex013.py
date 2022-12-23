salario = float(input('Digite o salário do funcionário: '))
porcentagem = int(input('Digite quanto de aumento em porcentagem o funcionário vai receber: '))
aumento = porcentagem / 100
atual = salario + (aumento*salario)
var = "%"
print('O salário do funcionario era R${:.2f} agora após o aumento de {}{} ele vai receber R${:.2f}'.format(salario,porcentagem,var,atual))