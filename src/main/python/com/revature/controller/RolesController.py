#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ControllerRoles
#By Bertrick

import logging
from service import RolesService, UsersService, AccountsService, TransactionsService
from entity import Roles, Users, Accounts, Transactions
from datetime import date
from error import Error

class Functionalities:

    #save new role
    def save(self, connection, cursor):
        
        name = raw_input("Role name : ")
        description = raw_input("Description : ")
        createdAt = str(date. today())
        updatedAt =  str(date. today())
        enabled = int(input("Status (enable 1 or deseable 0) "))
        role = Roles(name, description, createdAt, updatedAt, enabled)
        return RolesService.Init().save(role, connection, cursor)


    #delete role
    def delete(self, port):
           
        return 

    def getAllRoles(self, connection, cursor):

        return RolesService.Init().getAllRoles(connection, cursor)


    def  printAllRoles(self, roles, connection, cursor):

         for role in roles:
            print('''
                Role Name       =  {0}
                Description      = {1}
                Created date    =  {2}
                ''').format(role[2], role[4], role[5])




