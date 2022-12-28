str = str(input('Escreva uma frase: ')).strip()

lenght = len(str)
rev = -1
for x in range(0,lenght):
    if (str[x]) == (str[rev]):
        print(str[x],str[rev])
    elif str[x] == ' ':
        print('pulei')
        rev+=1
    elif str[rev] == ' ':
        print('pulei')
