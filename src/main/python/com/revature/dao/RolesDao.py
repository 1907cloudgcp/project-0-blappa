#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceRoles
#By Bertrick

import logging
import mysql.connector
from mysql.connector import Error


class Init:
  
    
	#save new role
	def save(self, user, connection, cursor):
	    
            return


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
