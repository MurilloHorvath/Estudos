limpa = '\033[m'
textred = '\033[31m'
textblue = '\033[36m'

c = float(input('Informe a temperatura em °C: {}'.format(textblue)))
f = ((c*9)/5) + 32
print('{}A temperatura de {}{}°C{} corresponde a {}{:.2f}°F{}!'.format(limpa,textblue,c,limpa,textred,f,limpa))
