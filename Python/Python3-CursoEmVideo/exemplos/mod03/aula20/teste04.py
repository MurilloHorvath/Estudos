def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    # for valor in num:
    #     print(f'{valor} ', end='')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)