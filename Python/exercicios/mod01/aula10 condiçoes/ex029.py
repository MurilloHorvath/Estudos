textred = '\033[31m'
textgreen = '\033[32m'
limpa = '\033[m'

vel = float(input('Qual é a velocidade do Veiculo: {}'.format(textgreen)))

if vel>80:
    print('{}{}Você foi multado...{} Seu veiculo está a cima da velocidade permitida.'.format(limpa,textred,limpa))
    multa = 7 * (vel - 80)
    print('A multa vai custar {}R${:.2f}{}'.format(textgreen,multa,limpa))
    
print('{}Tenha um bom dia, Dirija com segurança!'.format(limpa))