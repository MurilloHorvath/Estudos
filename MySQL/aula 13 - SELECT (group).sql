select totaulas from cursos
group by totaulas
order by totaulas;

select totaulas,count(*) from cursos
group by totaulas
order by totaulas;

select carga,count(*) from cursos where totaulas = 30
group by carga;