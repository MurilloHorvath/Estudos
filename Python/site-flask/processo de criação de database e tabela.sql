create database usuarios
default character set utf8
default collate utf8_general_ci;

create table usuario(

id int not null auto_increment,
nome varchar(30) not null,
senha varchar(10) not null,
primary key(id)

)default charset = utf8;

insert into usuario values(default,'Murillo','123');

select * from usuario;