#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceAccounts
#By Bertrick

import logging
from entity import Accounts, Transactions
import mysql.connector
from mysql.connector import Error
from dao import DaoAccounts

class Init:
  
	#create accounts
	def create(self, account, connection, cursor):

            return DaoAccounts.Init().create(account, connection, cursor)


	#update accounts
	def update(self, iduser, connection, cursor):

	    return 


	#delete accounts
	def delete(self, iduser, connection, cursor):

	    return 



	def deposit(self, users_id, account, balance, description, createdAt, updatedAt, connection, cursor):

             return DaoAccounts.Init().deposit(users_id, account, balance, description, createdAt, updatedAt, connection, cursor)


        def withdraw(self, users_id, account, balance, description, createdAt, updatedAt, connection, cursor):
        
             return DaoAccounts.Init().withdraw(users_id, account, balance, description, createdAt, updatedAt, connection, cursor)

    

        def getId(self, id, connection, cursor): 

	     return  DaoAccounts.Init().getId(id, connection, cursor)



        def getAccount(self, account_num, connection, cursor):

	     return DaoAccounts.Init().getAccount(account_num, connection, cursor)


