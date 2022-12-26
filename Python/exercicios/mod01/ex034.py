sal = float(input('Digite o salário do funcionario: '))

if sal>1250:
    aumt = sal + (sal * 0.10)
    print('Salario atual R${:.2f} apos o aumento R${:.2f}'.format(sal,aumt))
else:
    aumt = sal + (sal * 0.15)
    print('Salario atual R${:.2f} apos o aumento R${:.2f}'.format(sal,aumt))