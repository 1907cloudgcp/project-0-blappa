#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceTransactions
#By Bertrick

import logging
import mysql.connector
from mysql.connector import Error


class Init:
  

    
	#create transactions
	def save(self, transaction, connection, cursor):
	    try:   
		sql_insert_query = """ INSERT INTO transactions (isbn_13, name, description, typeTrs, startDate, endDate, createdAt, updatedAt, accounts_transactions_id, enabled) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

		insert_tuple = ("000"+transaction.name, transaction.name, transaction.description, transaction.typeTrs, transaction.startDate, transaction.endDate, transaction.createdAt, transaction.updatedAt, transaction.account_id, transaction.enabled)
	        result  = cursor.execute(sql_insert_query, insert_tuple)
 
                connection.commit()
                return True

            except mysql.connector.Error as error :
                connection.rollback()
	        return False


	#update transactions
	def update(self, iduser, connection, cursor):

	    return 


	#delete transactions
	def delete(self, iduser, connection, cursor):

	    return 


	def getId(self, id, connection, cursor): 

		query = """ SELECT id FROM transactions AS t WHERE t.id= '%s' """ % (id)

	        cursor.execute(query)

		isbn_13 = cursor.fetchall()

		return isbn_13[0][0]


        #get all transaction about specific account bank 
        def getAllPassTrs(self, account_id, connection, cursor):

                query = """ SELECT * FROM transactions AS t WHERE t.accounts_transactions_id= '%s' """ % (account_id)

                cursor.execute(query)

                alls = cursor.fetchall()

                return alls


        #get all  transactions
        def getAllTrs(self, connection, cursor):

                query = """ SELECT * FROM transactions"""

                cursor.execute(query)

                alls = cursor.fetchall()

                return alls


