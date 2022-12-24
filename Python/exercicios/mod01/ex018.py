from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo qualquer: '))

sen = sin(radians(angulo))
print('O seno de {:.0f}° é : {:.1f}°'.format(angulo,sen))
coss = cos(radians(angulo))
print('O cosseno de {:.0f}° é : {:.1f}°'.format(angulo,coss))
tang = tan(radians(angulo))
print('A tangente de {:.0f}° é : {:.1f}°'.format(angulo,tang))
