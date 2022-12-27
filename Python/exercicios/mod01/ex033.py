textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
limpa = '\033[m'

n1 = int(input('Primeiro valor: {}'.format(textyellow)))
n2 = int(input('{}Segundo valor: {}'.format(limpa,textyellow)))
n3 = int(input('{}Terceiro valor: {}'.format(limpa,textyellow)))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('{}O menor valor digitado foi {}{}{}'.format(limpa,textred,menor,limpa))
print('O maior valor digitado foi {}{}{}'.format(textgreen,maior,limpa))
