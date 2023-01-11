create table if not exists teste(
id int,
nome varchar(10),
idade int
);

insert into teste value
('1','Pedro','22'),
('2','Maria','19'),
('3','Paulo','30');

select * from teste;

drop table if exists teste;