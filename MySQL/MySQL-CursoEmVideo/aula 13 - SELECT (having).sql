select ano, count(*) from cursos
group by ano
having count(ano) >= 5
order by count(*);
# so pode utilizar o "having" com o mesmo parametro do "group" no caso acima é o parametro "ano"

select ano, count(*) from cursos
group by ano
having ano > 2016
order by count(*);

select ano, count(*) from cursos
where totaulas > 20
group by ano
having ano > 2013
order by count(*);

select carga,count(*) from cursos
where ano > 2015
group by carga
having carga > (select avg(carga) from cursos);