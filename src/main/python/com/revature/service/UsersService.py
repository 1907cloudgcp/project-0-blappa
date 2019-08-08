#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceUsers
#By Bertrick

import logging
from entity import Users
from dao import UsersDao


class Init:
  
    
	#create users
	def create(self, user, connection, cursor):
	    
            return UsersDao.Init().create(user, connection, cursor)


	#update user
	def update(self, iduser, connection, cursor):

	    return 


	#delete user
	def delete(self, iduser, connection, cursor):

	    return 


        def getId(self, id, connection, cursor): 

	    user_id =  UsersDao.Init().getId(id, connection, cursor)

	    return user_id


	#login user
	def login(self, username, pswd,connnection,  cursor):
	    
	    return UsersDao.Init().login(username, pswd, connnection,  cursor)


	#logout user
	def logout(self, connection, cursor):
                  
	    UsersDao.Init().logout(connection, cursor)  

