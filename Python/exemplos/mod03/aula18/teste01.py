teste = list()
teste.append('Murillo')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 20
galera.append(teste[:])
print(galera)