'''
str = str(input('Escreva uma frase: ')).strip().lower()
lenght = len(str)
meio = lenght // 2
n = []
res = 0
for x in range(0,lenght):
    if str[x] == ' ':
        continue
    else:
        n += str[x]
for x in range(0,meio):
    if n[x] == n[-x-1]:
        continue
    elif n[x] != n[-x-1]:
        print('Não é um Palíndromo')
        res+=1
        break
if res == 0:
    print('Está frase é um Palíndromo')
'''

'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palíndromo')
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palíndromo')