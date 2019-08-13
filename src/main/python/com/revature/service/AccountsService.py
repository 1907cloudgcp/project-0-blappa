#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceAccounts
#By Bertrick

import logging
from entity import Accounts, Transactions
from dao import AccountsDao

class Init:
  
	#create accounts
	def create(self, account, connection, cursor):

            return AccountsDao.Init().create(account, connection, cursor)


	#update accounts
	def update(self, iduser, connection, cursor):

	    return 


	#delete accounts
	def delete(self, iduser, connection, cursor):

	    return 



	def deposit(self, users_id, account, balance, description, createdAt, updatedAt, connection, cursor):

             return AccountsDao.Init().deposit(users_id, account, balance, description, createdAt, updatedAt, connection, cursor)


        def withdraw(self, users_id, account, balance, description, createdAt, updatedAt, connection, cursor):
        
             return AccountsDao.Init().withdraw(users_id, account, balance, description, createdAt, updatedAt, connection, cursor)

    

        def getId(self, id, connection, cursor): 

	     return  AccountsDao.Init().getId(id, connection, cursor)



        def getAccount(self, account_num, connection, cursor):

	     return AccountsDao.Init().getAccount(account_num, connection, cursor)


        #get all accounts
        def getAllAccounts(self, connection, cursor):
             return  AccountsDao.Init().getAllAccounts(connection, cursor)




