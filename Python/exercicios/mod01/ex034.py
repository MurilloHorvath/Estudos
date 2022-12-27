textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

sal = float(input('Digite o salário do funcionario: {}R$ '.format(textgreen)))
if sal>1250:
    aumt = sal + (sal * 0.10)
else:
    aumt = sal + (sal * 0.15)
print('{}Salario antigo {}R${:.2f}{} apos o aumento {}R${:.2f}{}'.format(limpa,textred,sal,limpa,textgreen,aumt,limpa))