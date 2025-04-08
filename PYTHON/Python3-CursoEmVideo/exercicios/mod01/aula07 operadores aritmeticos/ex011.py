textred = '\033[31m'
textpurple = '\033[34m'
textpink = '\033[35m'
limpa = '\033[m'

largura = float(input('Digite a largura da parede em metros: {}'.format(textred)))
altura = float(input('{}Digite a altura da parede em metros: {}'.format(limpa,textred)))
area = largura * altura #resultado vai ser em m²
tinta = area / 2
print('{}A área da parede é {}{:.3f}m²{} e a quantida necessaria de tinta é de {}{:.3f} Litros{}'.format(limpa,textpurple,area,limpa,textpink,tinta,limpa))
