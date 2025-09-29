boletim = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    boletim.append([nome,[nota1,nota2],media])
    cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while cont not in 'NnSs':
        cont = str(input('Tente novamente. Deseja continuar? [S/N]')).upper().strip()[0]
    if cont in 'Nn':
        print('Analisando notas..')
        break

print('-'*30)
print(f'{"N°":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-'*26)

for c in range(0,len(boletim)):
    print(f'{c:<4}{boletim[c][0]:<10}{boletim[c][2]:>8}')
print('-'*26)

while True:
    esp = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if esp == 999:
        print('Finalizando..')
        break
    if esp <= len(boletim)-1:
        print(f'As notas de {boletim[esp][0]} são {boletim[esp][1]}')
        print('-'*26)
