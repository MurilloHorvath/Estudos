pessoas = {'nome':'Murillo','sexo':'M','idade':19}
pessoas['nome'] = 'Ricardo'
pessoas['idade'] = 55
pessoas['peso'] = 90
for k,v in pessoas.items():
    print(f'{k} = {v}')