drop table if exists bank_p0;

create table roles (
  isbn_13 varchar (13) primary key,
  name varchar (100),
  roles varchar (80),
  description varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  enabled boolean
);

insert into roles values ('1111111','ADMIN','administrator','create_update_delete','10/12/95','10/12/95','1');

create table users (
  isbn_13 varchar (13) primary key,
  name varchar (100),
  email varchar (80),
  phnumber varchar (80),
  birth_date varchar (80),
  username varchar (80),
  pswd varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  roles_users_isbn_13  varchar (80),
  enabled boolean,
  foreign key(roles_users_isbn_13) references roles(isbn_13)
);

insert into users values ('1111111','Bertrick Lappa','bertricklappa@gmail.com','4054762371','10/12/95','blappa','xx123','10/12/95','10/12/95','1111111','1');  


create table accounts (
  isbn_13 varchar (13) primary key,
  account_name varchar (100),
  account_num varchar (80),
  typeA varchar (80),
  description varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  users_accounts_isbn_13  varchar (80),
  enabled boolean,
  foreign key(users_accounts_isbn_13) references users(isbn_13)
);


create table transactions (
  isbn_13 varchar (13) primary key,
  name varchar (100),
  description varchar (80),
  typeTrs varchar (80),
  creation_date varchar (80),
  startDate varchar (80),
  endDate varchar (80),
  createdAt varchar (80),
  updatedAt varchar (80),
  accounts_transactions_isbn_13  varchar (80),
  enabled boolean,
  foreign key(accounts_transactions_isbn_13) references accounts(isbn_13)
);
