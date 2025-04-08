textred = '\033[31m'
textgreen = '\033[32m'
textyellow = '\033[33m'
textpurple = '\033[34m'
textpink = '\033[35m'
textblue = '\033[36m'
limpa = '\033[m'

m = int(input('Digite uma distância em metros: {}'.format(textgreen)))
print('{}{}A medida de {}m corresponde a{}'.format(limpa,textred,m,limpa))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('{}{} km{}'.format(textred,km,limpa))
print('{}{} hm{}'.format(textgreen,hm,limpa))
print('{}{} dam{}'.format(textyellow,dam,limpa))
print('{}{} dm{}'.format(textpurple,dm,limpa))
print('{}{} cm{}'.format(textpink,cm,limpa))
print('{}{} mm{}'.format(textblue,mm,limpa))
