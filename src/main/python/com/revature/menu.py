#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#menu App
#By Bertrick

import logging
from controller import RolesController, UsersController, AccountsController, TransactionsController
from error import Error

#welcome function
def show_menu(connection, cursor):

    logging.basicConfig(filename='../../../resources/app.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)   
    
    menu ='''
    Main menu: 
    -----------------------------------------------------------
    ->> For register, press 1. 
    ->> For create account, press 2.
    ->> To make deposit, press 3.
    ->> For withdraw, press 4.
    ->> For check balance, press 5.
    ->> For check bank account informations, press 6.
    ->> For view all past transactions, press 7.
    ->> For view all transaction, press 8.
    ->> To create new role, press 9.
    ->> For view all users, press 10.
    ->> For view all accounts, press 11.
    ->> For view all roles, press 12.
    >>>
    ->> To leave menu, press 0.
    >>> \n
    '''

    choice = int(input(menu))
    
    #users registering
    if choice == 1:
        try:
           print("Please, complete information below : \n-- User registering : ")  
        
           #get all user controller
           usersController = UsersController.Functionalities()
           result = usersController.save(connection, cursor)

           print("\nUser saved successfully !\n")
           logging.info('save user successfully')

        except Error:
             raise Error("Registering user failure!")
             print(e.value)
             logging.error(e.value)

    #registering an account
    if choice == 2:
         try:     
	    print("Please, complete information below : \n-- Account registering : ")  
        
            #get all account controller
            accountsController = AccountsController.Functionalities()
            result = accountsController.save(connection, cursor)

            print("\nAccount saved successfully !\n")
            logging.info('account user save successfully')

         except Error as e:
            raise Error("Registering failure!")
            print(e.value)      


    #deposit into account bank
    if choice == 3:
         try:
             print("Please, complete information below : \n-- Make a deposit into account : ")  
     
             #get functionnalities from account controller
             accountsController = AccountsController.Functionalities()
             result = accountsController.deposit(connection, cursor)
                     
             print("\ndeposit made successfully !\n")
             logging.info('deposit made successfully')

         except Error as e:
             raise Error("Registering failure!")
             print(e.value)
     
    #withdraw into account
    if choice == 4:
           try:
              print("Please, complete information below : \n-- Withdraw into account : ")  
     
        
              accountsController = AccountsController.Functionalities()
              result = accountsController.withdraw(connection, cursor)
                     
              print("\nWithdraw made successfully !\n")
              logging.info('withdraw made successfully')

           except Error as e:
              raise Error("Registering failure!")
              print(e.value)
    

    #print my balance
    if choice == 5:
           try: 
              acc_num = raw_input("Please, enter the account number : ")

              accountsController = AccountsController.Functionalities()
              result = accountsController.viewBalance(acc_num, connection, cursor)

              print ("\nPlease, follow your balance : "+result)
              print("\n")

           except Error as e:
              raise Error("Account number not found!\n Please check and try again later!!")
              print(e.value)
  
    #print my account bank informations
    if choice == 6:
           try:
              acc_num =  raw_input("Please, enter the account number : ")

              accountsController = AccountsController.Functionalities()
              result = accountsController.view(acc_num, connection, cursor)

              print ("\nPlease, below your account bank informations ")

              accountsController.printA(result, connection, cursor)

           except Error as e:
              raise Error("Account number not found!\n Please check and try again later!!")
              print(e.value)


    #view all my pass transactions
    if choice == 7:
           try:
              transactionsController = TransactionsController.Functionalities()
              account_num = raw_input("Please, enter your account bank number : ")
       
              result = transactionsController.getAllPassTrs(account_num, connection, cursor)
         
              print ("\nPlease, find below all your pass transactions \n")
         
              transactionsController.printAllTrs(result, connection, cursor)

           except Error as e:
              raise Error("Account number not found!\n Please check and try again later!!")
              print(e.value)


    #view all transactions
    if choice == 8:
          transactionsController = TransactionsController.Functionalities()
          result = transactionsController.getAllTrs(connection, cursor)

          print ("\nPlease, below the list of all transactions \n")

          transactionsController.printAllTrs(result, connection, cursor)


    if choice == 9:
         print("Please, complete form below : \n-- save new role : ")
         rolesController = RolesController.Functionalities()
         result =  rolesController.save(connection, cursor)

         print("\nRole saved successfully !\n")
         logging.info('Role save successfully')
    

    #view all users
    if choice == 10:
          usersController = UsersController.Functionalities()
          results = usersController.getAllUsers(connection, cursor)

          print ("\nPlease, below the list of all users \n")

          usersController.printAllUsers(results, connection, cursor)


    #print all accounts
    if choice == 11:
          accountsController = AccountsController.Functionalities()
          results = accountsController.getAllAccounts(connection, cursor)

          print ("\nPlease, below the list of all accounts \n")

          accountsController.printAllAccounts(results, connection, cursor)


        
    if choice == 12:
          rolesController = RolesController.Functionalities()
          results = rolesController.getAllRoles(connection, cursor)

          print ("\nPlease, below the list of all roles \n")

          rolesController.printAllRoles(results, connection, cursor)


