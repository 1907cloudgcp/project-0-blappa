drop table if exists bank_p0;

create table users (
  isbn_13 varchar (13) primary key,
  name varchar (100),
  email varchar (80),
  phnumber varchar (80),
  login varchar (80),
  pswd varchar (80),
  status boolean
);

insert into users values ('1111111','Bertrick Lappa','bertricklappa@gmail.com','4054762371','blappa','xx123','1');







   
