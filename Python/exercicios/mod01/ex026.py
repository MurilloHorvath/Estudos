frase = str(input('Digite uma frase: ')).upper().strip()

print('Quantas letras A tem na frase?', frase.count('A'))
print('Em qual posição ela aparece pela primeira vez?', frase.find('A') + 1)
print('Em qual posição ela aparece pela ultima vez?', frase.rfind('A') + 1)
