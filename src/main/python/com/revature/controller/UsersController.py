#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ControllerUsers
#By Bertrick

import logging
from service import RolesService, UsersService, AccountsService, TransactionsService
from entity import Roles, Users, Accounts, Transactions
from datetime import date


class Functionalities:

    #save user
    def save(self, connection, cursor):

        name = raw_input("Name : ")
        email = raw_input("Email : ")
        phnumber = raw_input("Phone Number : ")
        birth_date = raw_input("Birth Date : ")
        username = raw_input("Login : ")
        pswd = raw_input("Password : ")
        createdAt = str(date. today())
        updatedAt =  str(date. today())
        roles_users_isbn_13 = int(raw_input("Role ID : "))
        enabled = int(input("Status (enable 1 or deseable 0) "))

        #get role ID
        role_id = RolesService.Init().getId(roles_users_isbn_13, connection, cursor)

        user = Users(name, email, phnumber, birth_date, username, pswd, createdAt, updatedAt, enabled, role_id)
                    
        result = UsersService.Init().create(user, connection, cursor)

        return result


    #login controller
    def login(self, username, pswd, connection, cursor):
  
        return UsersService.Init().login(username, pswd, connection, cursor)
 

    #logout controller
    def logout(self, connection, cursor):

        UsersService.Init().logout(connection, cursor)

    

   
