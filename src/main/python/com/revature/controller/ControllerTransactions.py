#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#ControllerTransactions
#By Bertrick

import logging
from service import ServiceRoles, ServiceUsers, ServiceAccounts, ServiceTransactions
from entity import Roles, Users, Accounts, Transactions
from datetime import date


class Functionalities:

    #get all trs about specific account
    def getAllPassTrs(self, account_num, connection, cursor):      

        account = ServiceAccounts.Init().getAccount(account_num, connection, cursor)
        result = ServiceTransactions.Init().getAllPassTrs(account[0], connection, cursor)

        return result


    #get all transactions
    def getAllTrs(self, connection, cursor):

        result = ServiceTransactions.Init().getAllTrs(connection, cursor)
        return result  

  
    def printAllTrs(self, transactions, connection, cursor):
         count = 0 
         for trs in transactions:
            print("-- trs"+str(count)+" --")
            print(trs)
            count += 1 
         print("\n")

