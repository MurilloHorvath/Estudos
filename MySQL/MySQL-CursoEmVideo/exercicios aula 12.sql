select * from gafanhotos;
#ex 01
select * from gafanhotos where sexo = 'F';

#ex 02
select * from gafanhotos 
where nascimento between '2000-01-01' and'2015-12-31' 
order by nome;

#ex 03
select nome from gafanhotos
where profissao = 'Programador';

#ex 04
select * from gafanhotos
where sexo = 'F' and nacionalidade = 'Brasil' and nome like 'J%';

#ex 05
select nome,nacionalidade from gafanhotos
where nome like '%Silva%' and nacionalidade != 'Brasil' and peso<80 and sexo = 'M';

#ex 06
select max(altura) from gafanhotos
where nacionalidade = 'Brasil' and sexo = 'M';

#ex 07
select avg(peso) from gafanhotos;

#ex 08
select min(peso) from gafanhotos
where sexo = 'F' and nacionalidade != 'Brasil' and nascimento between '1990-01-01' and '2000-12-31';

#ex 09
select count(altura) from gafanhotos
where sexo = 'F' and altura>'1.90';
