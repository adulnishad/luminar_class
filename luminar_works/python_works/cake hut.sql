create database cakehut;
use cakehut;

create table cake(
	id int auto_increment primary key,
    name varchar(200) not null 
	
);


insert into cake(name) values('white forest'),('blue berry'),('white chocoberry cake');

select * from cake;


create table cakevarient(

	id int auto_increment primary key,
    weight enum('1kg','2kg','3kg','4kg','5kg') default "1kg",
    price int not null,
    flavour varchar(200) not null,
    shape enum("round","rectangle","triangle","heart") default"round",
    cake_id int,
    foreign key(cake_id) references cake(id) on delete cascade,
    unique(weight,price,flavour,shape)
    
);

