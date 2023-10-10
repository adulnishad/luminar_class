show databases;
create database hotel;
use hotel;
create table items(
                  id int unique,
                  name varchar(100) not null,
                  catagory varchar(1500) not null,
                  price int not null,
                  type varchar(160) not null
		
                  );
                  
  -- listing tables---                
show tables;

-- inserting records--

insert into items(id,name,catagory,price,type) values(4,'noodles','non_veg',130,'indian');
select * from items;
select name,price from items;

-- fetch all records --

select * from items;

select name,price from items;

-- select items aviliable under rs 160--
select * from items where price < 160;

select * from items where price < 150 and price > 160;

select name from items where name !="chinees";

select count(*) from items;
select max(price) from items;
select sum(price) from items;
select * from items where price =(select max(price) from items);

select * from items where price =(select min(price) from items);
 select * from items where price =(select max(price) from items where catagory ="non_veg");


select  max(price) from items where price =(select max(price) from items);

select * from items where price =(select max(price) from items where price =(select max(price) from items));


select cateragory,count(*) from items group by(catagory);

-- sorted records --
select * from items order by price desc;

-- limit--
select * from items order by price desc limit 3;


select count(*) from items where name="biriyani";

update items set price=170 where  id=3;
update items set catagory="non_veg" where id=4;

-- delete qurry--

delete from  items where id=1;

-- truncate items;  -- remove data from items stucture not remove--

-- drop  table items; -- remove all data and stucture--

alter table items add column course enum("main_course","starter","desert") default "main_course";


update  items set course="starter" where id=3;











create database cakebox;

