select max(carga) from cursos;

select max(totaulas) from cursos where ano = '2016';

select min(carga) from cursos;

select nome, min(totaulas) from cursos where ano = '2016';