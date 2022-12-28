n = int(input('Digite um valor inteiro: '))
s = 0
for c in range(1,n+1):
    if n%1 == 0 and n%c == 0:
        s+=1

if s == 2:
    print('O Número é PRIMO')
else:
    print('O Número NÃO é primo')