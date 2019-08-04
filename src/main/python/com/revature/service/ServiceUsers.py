#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceUsers
#By Bertrick

import logging
from entity import Users
import mysql.connector
from mysql.connector import Error


class Init:
  
    
	#create users
	def create(self, user, connection, cursor):
	    try:   
	         sql_insert_query = """ INSERT INTO users (isbn_13, name, email, phnumber, birth_date, username, pswd, createdAt, updatedAt, roles_users_id, enabled) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

	         insert_tuple = ("000"+user.name, user.name, user.email ,user.phnumber, user.birth_date, user.username, user.pswd, user.createdAt, user.updatedAt, user.role_id, user.enabled)
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


        def getId(self, id, connection, cursor): 

            query = """ SELECT id FROM users AS u WHERE u.id= '%s' """ % (id)

	    cursor.execute(query)

	    isbn_13 = cursor.fetchall()

	    return isbn_13[0][0]


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

