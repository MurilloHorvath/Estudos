largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura #resultado vai ser em m²
tinta = area / 2
print('A área da parede é {:.3f}m² e a quantida necessaria de tinta é de {:.3f} Litros'.format(area,tinta))
