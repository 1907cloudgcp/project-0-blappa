#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceTransactions
#By Bertrick

import logging
import mysql.connector
from mysql.connector import Error
from dao import DaoTransactions

class Init:
  

    
	#create transactions
	def save(self, transaction, connection, cursor):
	   
            return DaoTransactions.Init().save(transaction, connection, cursor)


	#update transactions
	def update(self, iduser, connection, cursor):

	    return 


	#delete transactions
	def delete(self, iduser, connection, cursor):

	    return 


	def getId(self, id, connection, cursor):

	    return DaoTransactions.Init().getId(id, connection, cursor)


        #get all transaction about specific account bank 
        def getAllPassTrs(self, account_id, connection, cursor):
            
             return DaoTransactions.Init().getAllPassTrs(account_id, connection, cursor)


        #get all  transactions
        def getAllTrs(self, connection, cursor):
                
             return DaoTransactions.Init().getAllTrs(connection, cursor)
                
