#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ControllerUsers
#By Bertrick

import logging
from service import RolesService, UsersService, AccountsService, TransactionsService
from entity import Roles, Users, Accounts, Transactions
from datetime import date
from error import Error


class Functionalities:

    #save user
    def save(self, connection, cursor):
      try:
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
      except:
            raise Error("Registering User failure in User Controller!")
            logging.error(Error.value)


    #login controller
    def login(self, username, pswd, connection, cursor):
        try:      
             return UsersService.Init().login(username, pswd, connection, cursor)
        except Error as e:
             raise Error("login failure in User controller")
             #print(e.value)
             logging.error('e.value')


    #logout controller
    def logout(self, connection, cursor):
       try:
            UsersService.Init().logout(connection, cursor)
       except Error as e:
             raise Error("Logout failure in user controller!")
             print(e.value)
             logging.error('e.value')


    #get all users
    def getAllUsers(self, connection, cursor):
        return   UsersService.Init().getAllUsers(connection, cursor)


    def printAllUsers(self, users, connection, cursor):
         
         for user in users:
            print('''
                User Name       = {0}
                Email           = {1}
                Phone number    = {2}
                Birth date      = {3}
                Username        = {4}
                Created date    = {5}
                ''').format(user[2], user[3],user[4],  user[5], user[6], user[8])

