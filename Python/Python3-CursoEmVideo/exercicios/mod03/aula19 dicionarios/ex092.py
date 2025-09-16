from datetime import date

dados = dict()
dados['Nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - anonasc
dados['CTPS'] = int(input('Carteira de Trabalho: ( 0 não possui) '))
if dados['CTPS'] != 0:
    dados['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] +  (35-(date.today().year - dados['Ano de Contratação']))
print('-'*50)
print(dados)
for k,v in dados.items():
    print(f'{k}: {v}')