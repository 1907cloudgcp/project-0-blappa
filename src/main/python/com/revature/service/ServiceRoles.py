#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceRoles
#By Bertrick

import logging
from dao import DaoRoles

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

	    role_id = DaoRoles.Init().getId(id, connection, cursor)

            return role_id

