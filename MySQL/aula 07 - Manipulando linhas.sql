insert into cursos values
('1','HTML4','Curso de HTML5','40','37','2014'),
('2','Algaritmos','Lógica de Programação','20','15','2014'),
('3','Photoshop','Dicas de Photoshop CC','10','8','2014'),
('4','PGP','Curso de PHP para iniciantes','40','20','2010'),
('5','Jarva','Introdução à Linguagem Java','10','29','2000'),
('6','MySQL','Bancos de Dados MySQL','30','15','2016'),
('7','Word','Curso Completo de Word','40','30','2016'),
('8','SapateadO','Danças Ritmicas','40','30','2018'),
('9','Cozinha Gaúcha','Aprenda a fazer Churrasco','40','30','2018'),
('10','Youtuber','Gerar polêmica e Ganhar inscritos','5','2','2018');

#---------------Manipulando as linhas----------------
update cursos
set nome = 'HTML5'
where idcurso = '1';

update cursos
set nome = 'PHP', ano = '2015'
where idcurso = '4';

update cursos
set nome = 'Java', carga = '40', ano = '2015'
where idcurso = '5'
limit 1;
#limit > Utilizado para indicar a quantidade de linhas que serão alteradas/modificadas

update cursos
set ano = '2050', carga = '800'
where ano = '2018';
#Para usar essa instrução para alterar mais de uma linha
#é preciso desabilitar o modo de segurança..
# Edit > Preferences > SQL Editor > Desabilitar "Safe Updates"
# É recomendado deixar Habilitado
#ou fazer um backup do banco de dados para utilizar essa instrução

#-------------Deletando as linhas---------------
delete from cursos
where idcurso='10';

delete from cursos
where ano='2050'
limit 2;
#Também é desabilatar a opção "Safe Updates" para usar essa instrução

#---------------Deletando TODAS as linhas da tabela..------------------
truncate table cursos;

select * from cursos;