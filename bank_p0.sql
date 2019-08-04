drop table if exists bank_p0;

create table roles (
  id int primary key NOT NULL AUTO_INCREMENT,
  isbn_13 varchar (13),
  name varchar (100),
  roles varchar (80),
  description varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  enabled boolean
);

insert into roles(isbn_13,name, roles, description, createdAt, updatedAt,enabled) values ('1111111','ADMIN','administrator','create_update_delete','10/12/95','10/12/95','1');

create table users (
  id int primary key NOT NULL AUTO_INCREMENT,
  isbn_13 varchar (13),
  name varchar (100),
  email varchar (80),
  phnumber varchar (80),
  birth_date varchar (80),
  username varchar (80),
  pswd varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  roles_users_id  int,
  enabled boolean,
  foreign key(roles_users_id) references roles(id)
);

insert into users( isbn_13,name,email,phnumber,birth_date,username,pswd,createdAt,updatedAt,roles_users_id, enabled) values ('1111111','Bertrick Lappa','bertricklappa@gmail.com','4054762371','10/12/95','blappa','xx123','10/12/95','10/12/95',1,'1');  


create table accounts (
  id int primary key NOT NULL AUTO_INCREMENT,
  isbn_13 varchar (13),
  account_name varchar (100),
  account_num varchar (80),
  balance char(20),
  typeA varchar (80),
  description varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  users_accounts_id int,
  enabled boolean,
  foreign key(users_accounts_id) references users(id)
);


create table transactions (
  id int primary key NOT NULL AUTO_INCREMENT,
  isbn_13 varchar (13),
  name varchar (100),
  description varchar (80),
  typeTrs varchar (80),
  startDate varchar (80),
  endDate varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  accounts_transactions_id  int,
  enabled boolean,
  foreign key(accounts_transactions_id) references accounts(id)
);
