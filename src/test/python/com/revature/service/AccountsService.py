#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ServiceAccounts
#By Bertrick

from entity import Accounts, Users

class Init:
  

    def deposit(self, user, account, balance, description, createdAt, updatedAt):

            newbalance =  account.balance + balance

            #save new balance after deposit
            account.balance = newbalance

            return newbalance

    def withdraw(self, users_id, account, balance, description, createdAt, updatedAt):
        
            newbalance =  account.balance - balance

            #save new balance after withdraw
            account.balance = newbalance

            return newbalance

