#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceUsers
#By Bertrick

import logging
from entity import Users
from dao import DaoUsers


class Init:
  
    
	#create users
	def create(self, user, connection, cursor):
	    
            return DaoUsers.Init().create(user, connection, cursor)


	#update user
	def update(self, iduser, connection, cursor):

	    return 


	#delete user
	def delete(self, iduser, connection, cursor):

	    return 


        def getId(self, id, connection, cursor): 

	    user_id =  DaoUsers.Init().getId(id, connection, cursor)

	    return user_id


	#login user
	def login(self, username, pswd,connnection,  cursor):
	    
	    return DaoUsers.Init().login(username, pswd, connnection,  cursor)


	#logout user
	def logout(self, connection, cursor):
                  
	    connection.close() 

