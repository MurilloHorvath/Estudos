peso = float(input('Digite o seu peso: kg '))
altura = float(input('Digite a sua altura: m '))

print('Calculando o seu IMC..')


imc = peso / (altura * altura)

if imc < 18.5:
    print('IMC: {:.2f} - Abaixo do peso'.format(imc))
elif imc < 25:
    print('IMC: {:.2f} - Peso ideal'.format(imc))
elif imc < 30:
    print('IMC: {:.2f} - Sobrepeso'.format(imc))
elif imc <= 40:
    print('IMC: {:.2f} - Obesidade'.format(imc))
elif imc > 40:
    print('IMC: {:.2f} - Obesidade mórbida'.format(imc))
else:
    print('ERRO')
