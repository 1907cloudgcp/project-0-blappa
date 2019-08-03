#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Register
#By Bertrick

import logging
from controller import Users, Accounts, Transactions, Roles
import mysql.connector
from mysql.connector import Error


class Init:
  
    
	#create users
	def create(self, user, connection, cursor):
	    try:   
		sql_insert_query = """ INSERT INTO users (isbn_13, name, email, phnumber, birth_date, username, pswd, createdAt, updatedAt, enabled) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

		insert_tuple = ("000"+user.name, user.name, user.email ,user.phnumber, user.birth_date, user.username, user.pswd, user.createdAt, user.updatedAt, user.enabled)
	        result  = cursor.execute(sql_insert_query, insert_tuple)
 
                connection.commit()
                return True

            except mysql.connector.Error as error :
        	connection.rollback()
	        return False


	#update user
	def update(self, iduser, connection, cursor):

	    return 


	#delete user
	def delete(self, iduser, connection, cursor):

	    return 


	#login user
	def login(self, username, pswd,connnection,  cursor):
	    
            query = """SELECT username, pswd FROM users AS u WHERE u.username= '%s' AND u.pswd = '%s' """ % (username, pswd)

            cursor.execute(query)

	    myresult = cursor.fetchall()
            
	    if myresult[0][0] == username and myresult[0][1] == pswd:
	    	return True
	    return False


	#logout user
	def logout(self, connection, cursor):

	    return 

