vel = int(input('Qual é a velocidade do Veiculo: '))

if vel>80:
    print('Você foi multado... Seu veiculo estava a cima da velocidade.')
    multa = 7 * (vel - 80)
    print('A multa vai custar R${:.2f}'.format(multa))