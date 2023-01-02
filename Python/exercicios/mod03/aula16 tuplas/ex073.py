brasileirao = ('Palmeiras','Internacional','Fluminense','Corinthians',
'Flamengo','Atlético-PR','Atlético-MG','Fortaleza','São Paulo','América-MG',
'Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá','Ceará SC','Atlético-GO',
'Avaí','Juventude')
for t in brasileirao:
    print(t)
print('Tabale Brasileirão 2022')
print('Os Primeiros colocados ',brasileirao[0:5])
print('Os últimos colocados ',brasileirao[-4:])
print('Os times em ordem alfabética ',sorted(brasileirao))
print(f'O Santos está na {brasileirao.index("Santos")+1}° posição')
# Tem que utilizar as aspas duplas por que ele esta dentro de outra aspas..