op=0
while op !=5:
    num1 = int(input('Digite o 1° Valor: '))
    num2 = int(input('Digite o 2° Valor: '))
    op = int(input('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Números
    [5]Sair do programa
    '''))
    if op == 1:
        res = num1 + num2
        print('A soma dos valores {} + {} = {}'.format(num1,num2,res))
    elif op == 2:
        res = num1 * num2
        print('A multiplicação dos valores {} x {} = {}'.format(num1,num2,res))
    elif op == 3:
        if num1>num2:
            print('O maior dos dois valores é {}'.format(num1))
        else:
            print('O maior dos dois valores é {}'.format(num2))
    elif op == 4:
        continue
    elif op == 5:
        print('Finalizando Programa')
    else:
        print('Opção invalida - Tente Novamente')
print('FIM')