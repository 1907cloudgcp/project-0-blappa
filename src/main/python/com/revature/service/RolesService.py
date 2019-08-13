#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceRoles
#By Bertrick

import logging
from dao import RolesDao

class Init:
  
    
	#save new role
	def save(self, role, connection, cursor):
	    
            return RolesDao.Init().create(role, connection, cursor)


	#update roles
	def update(self, iduser, connection, cursor):

	    return 


	#delete roles
	def delete(self, iduser, connection, cursor):

	    return  r


	def getId(self, id, connection, cursor): 

	    role_id = RolesDao.Init().getId(id, connection, cursor)

            return role_id

         
        def getAllRoles(self, connection, cursor):
            
            return RolesDao.Init().getAllRoles(connection, cursor) 

             
                
