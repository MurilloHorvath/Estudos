use cadastro;
describe gafanhotos;

alter table gafanhotos
add column cursopreferido int;

alter table gafanhotos
add foreign key (cursopreferido)
references cursos(idcurso);

select * from gafanhotos;
select * from cursos;

update gafanhotos set cursopreferido = '6' where id = '1';

delete from cursos where idcurso = '6';
#Não é possivel deletar o curso pois ele está relacionado ao Gafanhoto de id = '1'
#Só é possivel deletar se esse curso não estiver relacionado a algum gafanhoto