import time
num1 = int(input('Digite o 1° Valor: '))
num2 = int(input('Digite o 2° Valor: '))
op=0
while op !=5:
    op = int(input('''[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do programa
Qual é a sua opçaõ? '''))
    if op == 1:
        res = num1 + num2
        print('A soma dos valores {} + {} = {}'.format(num1,num2,res))
    elif op == 2:
        res = num1 * num2
        print('A multiplicação dos valores {} x {} = {}'.format(num1,num2,res))
    elif op == 3:
        if num1>num2:
            maior = num1
        else:
            maior = num2
        print('Entre os valores {} e {} o maior é {}'.format(num1,num2,maior))
    elif op == 4:
        print('Informe os números novamente:')
        num1 = int(input('Digite o 1° Valor: '))
        num2 = int(input('Digite o 2° Valor: '))
    elif op == 5:
        print('Finalizando Programa..')
    else:
        print('Opção invalida - Tente Novamente')
    print('=-='*15)
    time.sleep(2)
print('FIM')