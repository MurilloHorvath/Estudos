num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    esc = int(input('Digite um número de 0 a 20: '))
    while  esc>20 or esc<0:
        esc = int(input('Tente novamente.Digite um número de 0 a 20: '))
        
    print(f'O número escolhido foi {esc} escrito por extenso {num[esc]}.')
    
    cont = str(input('Voce deseja continuar? [S/N]'))
    if cont in 'Nn':
        print('Finalizando o programa..')
        break 