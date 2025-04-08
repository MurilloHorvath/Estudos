pessoas = {'nome':'Murillo','sexo':'M','idade':19}
print(pessoas)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} Anos.')
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k,v in pessoas.items():
    print(f'{k} = {v}')