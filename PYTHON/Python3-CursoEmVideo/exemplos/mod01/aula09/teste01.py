print("""Lorem ipsum dolor sit amet. Sed reprehenderit voluptates et omnis eligendi et facilis nisi 
est neque pariatur ut autem libero aut inventore voluptatem est officiis autem. Sed labore minus At velit 
quia nam sint doloremque ut quod praesentium eos ratione necessitatibus. Ut fuga voluptatem ut quasi minima ut veritatis 
ducimus cum dicta molestiae id corporis perspiciatis hic voluptatibus officiis.""")

frase = 'Curso em Video Python'

#Fatiamento
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Aprenda Python  '
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

#Divisão
frase = 'Curso em Video Python'
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][2])

#Junção
print('-'.join(frase))
