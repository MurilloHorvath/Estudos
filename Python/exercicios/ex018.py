import math
angulo = float(input('Digite um ângulo qualquer: '))

sen = math.sin(math.radians(angulo))
print('O seno de {:.0f}° é : {:.1f}°'.format(angulo,sen))
cos = math.cos(math.radians(angulo))
print('O cosseno de {:.0f}° é : {:.1f}°'.format(angulo,cos))
tan = math.tan(math.radians(angulo))
print('A tangente de {:.0f}° é : {:.1f}°'.format(angulo,tan))
