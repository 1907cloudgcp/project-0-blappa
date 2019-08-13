#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceRoles
#By Bertrick

import logging
import mysql.connector
from mysql.connector import Error


class Init:
  
    
	#save new role
	def create(self, role, connection, cursor):
	    sql_insert_query = """ INSERT INTO roles (isbn_13, name, description, createdAt, updatedAt, enabled) VALUES (%s,%s,%s,%s,%s,%s)"""
            insert_tuple = ("000"+role.name, role.name, role.description , role.createdAt, role.updatedAt, role.enabled)
            result  = cursor.execute(sql_insert_query, insert_tuple)
            connection.commit()
            return result


	#update roles
	def update(self, iduser, connection, cursor):

	    return 


	#delete roles
	def delete(self, iduser, connection, cursor):

	    return 


	def getId(self, id, connection, cursor): 

            query = """ SELECT id FROM roles AS r WHERE r.id= '%s' """ % (id)

	    cursor.execute(query)

	    isbn_13 = cursor.fetchall()

            return isbn_13[0][0]


        
        def getAllRoles(self, connection, cursor):

            query = """ SELECT * FROM roles """

            cursor.execute(query)

            return cursor.fetchall()

            
