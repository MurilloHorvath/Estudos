n = int(input('Digite um número de 0 a 9999:'))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o número ', n)
print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)