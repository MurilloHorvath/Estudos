palavras = ('Aprender','Programar','Linguagem','Python','Curso','Gratis','Estudar','Praticar','Trabalhar','Mercado','Programador','Futuro')

for c in palavras:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')