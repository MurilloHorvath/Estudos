boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
if boletim['media'] >= 7:
    boletim['situacao'] = 'APROVADO'
else:
    boletim['situacao'] = 'REPROVADO'

for a,b in boletim.items():
    print(f'{a} é igual a {b}')
