print('\033[4;37;40mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b))

nome = 'Murillo'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[1;36;40m',nome,'\033[m'))

nome = 'Murillo'
cores = {'limpa':'\033[m',
        'azul':'\033[36m',
        'amarelo':'\033[33m', 
        'pretobranco':'\033[7;37m'}
print('Prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))