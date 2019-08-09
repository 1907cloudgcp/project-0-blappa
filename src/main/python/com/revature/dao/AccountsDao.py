#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceAccounts
#By Bertrick

import logging
from entity import Accounts, Transactions
import mysql.connector
from mysql.connector import Error


class Init:
  
	#create accounts
	def create(self, account, connection, cursor):
	    try:   
		 sql_insert_query = """ INSERT INTO accounts (isbn_13, account_name, account_num, balance, typeA, description, createdAt, updatedAt,users_accounts_id, enabled) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

		 insert_tuple = ("000"+account.account_name, account.account_name, account.account_num, account.balance, account.typeA, account.description, account.createdAt, account.updatedAt, account.user_id, account.enabled)
	         result  = cursor.execute(sql_insert_query, insert_tuple)
 
                 connection.commit()
                 return result

            except mysql.connector.Error as error :
                 connection.rollback()
	         return False
            except Error as e:
               raise Error("Save account failure in Account dao!")
               print(e.value)
               logging.error('e.value')


	#update accounts
	def update(self, iduser, connection, cursor):

	    return 


	#delete accounts
	def delete(self, iduser, connection, cursor):

	    return 



	def deposit(self, users_id, account, balance, description, createdAt, updatedAt, connection, cursor):
           try:
               balance = str(float(account[4]) + balance)
        
               sql_update_query = """UPDATE accounts AS a SET a.balance = '%s' WHERE a.id = '%s' """ % (balance, account[0])

               cursor.execute(sql_update_query)

               connection.commit()

               return True
           except mysql.connector.Error as error :
                 connection.rollback()
           except Error as e:
               raise Error("Deposit failure in Account dao!")
               print(e.value)
               logging.error('e.value')


        def withdraw(self, users_id, account, balance, description, createdAt, updatedAt, connection, cursor):
            try:
                 balance = str(float(account[4]) - balance)
        
                 sql_update_query = """UPDATE accounts AS a SET a.balance = '%s' WHERE a.id = '%s' """ % (balance, account[0])

                 cursor.execute(sql_update_query)

                 connection.commit()

                 return True
            except Error as e:
               raise Error("Withdraw failure in Account dao!")
               print(e.value)
               logging.error('e.value')
    

        def getId(self, id, connection, cursor): 

             query = """ SELECT id FROM accounts AS a WHERE a.id= '%s' """ % (id)

	     cursor.execute(query)

             isbn_13 = cursor.fetchall()

	     return isbn_13[0][0]



        def getAccount(self, account_num, connection, cursor):

             query = """ SELECT * FROM accounts AS a WHERE a.account_num= '%s' """ % (account_num)

	     cursor.execute(query)

	     isbn_13 = cursor.fetchall()

	     return isbn_13[0]


