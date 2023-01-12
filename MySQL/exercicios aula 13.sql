#ex 01
select profissao,count(*) from gafanhotos
group by profissao;

#ex 02
select sexo,count(*) from gafanhotos
where nascimento > '2005-01-01'
group by sexo;

#ex 03
select nacionalidade,count(*) from gafanhotos
where nacionalidade != 'Brasil'
group by nacionalidade
having count(nacionalidade)>=3;

#ex 04
select altura,count(*) from gafanhotos
where peso > 100
group by altura
having altura>(select avg(altura) from gafanhotos);
