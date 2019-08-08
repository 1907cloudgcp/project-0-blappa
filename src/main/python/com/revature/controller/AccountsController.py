#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ControllerAccounts
#By Bertrick

import logging
from service import RolesService, UsersService, AccountsService, TransactionsService
from entity import Roles, Users, Accounts, Transactions
from datetime import date


class Functionalities:

    #save new account
    def save(self, connection, cursor):

        account_name = raw_input("Account name : ")
        account_num = raw_input("Account number : ")
        balance = raw_input("Balance (US): ")
        typeA = raw_input("Type account : ")
        description = raw_input("Description : ")
        createdAt = str(date. today())
        updatedAt =  str(date. today())
        users_id =int(raw_input("USER ID : "))
        enabled = int(input("Status (enable 1 or deseable 0) "))
        
        #get user ID
        user_id = UsersService.Init().getId(users_id, connection, cursor)
       
        account = Accounts(account_name, account_num, balance, typeA, description, createdAt, updatedAt, enabled, user_id)
                     
        result = AccountsService.Init().create(account, connection, cursor)

        return result


    #make a deposite 
    def deposit(self, connection, cursor):

        account_num = raw_input("Account number : ")
        balance = float(raw_input("Amount : "))
        typeTrs = raw_input("Type of trsaction: ")
        description = raw_input("Description : ")
        createdAt = str(date. today())
        updatedAt =  str(date. today())
        users_id = int(raw_input("USER ID : "))
        
        #get user ID
        user_id = UsersService.Init().getId(users_id, connection, cursor)
        
        #get account
        account = AccountsService.Init().getAccount(account_num, connection, cursor)
                
        #make a deposit
        result = AccountsService.Init().deposit(users_id, account, balance, description, createdAt, updatedAt, connection, cursor)
        startDate = createdAt
        endDate = updatedAt
        transaction = Transactions(account[1], description, typeTrs, startDate, endDate, createdAt, updatedAt, 1, account[0])

        result = TransactionsService.Init().save(transaction, connection, cursor)
        
        return result


    #withdraw controller
    def withdraw(self, connection, cursor):
        
        account_num = raw_input("Account number : ")
        balance = float(raw_input("Amount : "))
        typeTrs = raw_input("Type of trsaction: ")
        description = raw_input("Description : ")
        createdAt = str(date. today())
        updatedAt =  str(date. today())
        users_id = int(raw_input("USER ID : "))
        
        #get user ID
        users_id = UsersService.Init().getId(users_id, connection, cursor)
        
        #get account
        account = AccountsService.Init().getAccount(account_num, connection, cursor)
        
        #make a deposit
        result = AccountsService.Init().withdraw(users_id, account, balance, description, createdAt, updatedAt, connection, cursor)
        startDate = createdAt
        endDate = updatedAt
        transaction = Transactions(account[1], description, typeTrs, startDate, endDate, createdAt, updatedAt, 1, account[0])

        result = TransactionsService.Init().save(transaction, connection, cursor)
        
        return result


    def view(self, acc_num, connection, cursor):
       
        #get account
        account = AccountsService.Init().getAccount(acc_num, connection, cursor)
        
        return account

    
    def viewBalance(self, acc_num, connection, cursor):

        #get account
        account = AccountsService.Init().getAccount(acc_num, connection, cursor)

        return account[4]


    def  printA(self, account, connection, cursor):
         print('''
                Account name    = {0}
                Account number  = {1}
                Balance         = {2}
                Account type    = {3}
                Description     = {4}
                Created date    = {5}
                Updated date    = {6}
                Enabled         = {7}
                ''').format(account[2], account[3],account[4],  account[5], account[6], account[7], account[8], account[9])
    

                






