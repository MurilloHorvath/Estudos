from math import radians, sin, cos, tan

textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
textpurple = '\033[34m'
limpa = '\033[m'

angulo = float(input('Digite um ângulo qualquer: {}'.format(textred)))

sen = sin(radians(angulo))
print('{}O seno de {}{:.0f}°{} é : {}{:.1f}°{}'.format(limpa,textred,angulo,limpa,textgreen,sen,limpa))
coss = cos(radians(angulo))
print('O cosseno de {}{:.0f}°{} é : {}{:.1f}°{}'.format(textred,angulo,limpa,textyellow,coss,limpa))
tang = tan(radians(angulo))
print('A tangente de {}{:.0f}°{} é : {}{:.1f}°{}'.format(textred,angulo,limpa,textpurple,tang,limpa))
