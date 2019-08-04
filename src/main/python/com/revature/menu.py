#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#menu App
#By Bertrick

from controller import ControllerRoles, ControllerUsers, ControllerAccounts, ControllerTransactions

#welcome function
def show_menu(connection, cursor):
    
    menu ='''
    ->> For register, press 1. \n
    ->> For create account, press 2.\n
    ->> To make deposit money, press 3. \n
    ->> For withdraw money, press 4.\n
    ->> For view your balance, press 5.\n
    ->> For view my bank account, press 6.\n
    ->> For view all my past transactions, press 7.\n
    ->> For view all transaction, press 8.\n
    ->> For view all roles, press 9.\n
    ->> For view all users, press 10.\n
    ->> For view all accounts, press 11.\n
    ->> For logout, press 0. \n
    '''

    choice = int(input(menu))
    
    #users registering
    if choice == 1:

        print("Please, complete information below : \n-- User registering : ")  
        
         #get all user controller
        controllerUsers = ControllerUsers.Functionalities()
        result = controllerUsers.save(connection, cursor)

        if result:
           print("\nUser saved successfully !\n")
        else:
           print("\nRegistering failure! \n")

    #registering an account
    if choice == 2:
     	print("Please, complete information below : \n-- Account registering : ")  
        
        #get all account controller
        controllerAccounts = ControllerAccounts.Functionalities()
        result = controllerAccounts.save(connection, cursor)
        
        if result:
           print("\nAccount saved successfully !\n")
        else:
           print("\nRegistering failure! \n")

    #deposit into account bank
    if choice == 3:

        print("Please, complete information below : \n-- Make a deposit into account : ")  
     
        #get functionnalities from account controller
        controllerAccounts = ControllerAccounts.Functionalities()
        result = controllerAccounts.deposit(connection, cursor)
                     
        if result:
           print ("\nDeposit made successfully ")
        else:
           print("\nRegistering failure! \n")
     
    #withdraw into account
    if choice == 4:

        print("Please, complete information below : \n-- Withdraw into account : ")  
     
        
        controllerAccounts = ControllerAccounts.Functionalities()
        result = controllerAccounts.withdraw(connection, cursor)
                     
        if result:
           print ("\nWithdraw made successfully ")
        else:
           print("\nRegistering failure! \n")
    

    #print my balance
    if choice == 5:
       acc_num = raw_input("Please, enter the account number : ")

       controllerAccounts = ControllerAccounts.Functionalities()
       result = controllerAccounts.viewBalance(acc_num, connection, cursor)

       if result:
           print ("\nPlease, follow your balance : "+result)
           print("\n")

       else:
           print("\nAccount number not found!\n Please check and try again later! \n")
    
  
    #print my account bank informations
    if choice == 6:
       acc_num =  raw_input("Please, enter the account number : ")

       controllerAccounts = ControllerAccounts.Functionalities()
       result = controllerAccounts.view(acc_num, connection, cursor)

       if result:
           print ("\nPlease, below your account bank informations ")

           controllerAccounts.printA(result, connection, cursor)

       else:
           print("\nAccount number not found!\n Please check and try again later! \n")



    #view all my pass transactions
    if choice == 7:
        
        controllerTransactions = ControllerTransactions.Functionalities()
        account_num = raw_input("Please, enter your account bank number : ")
       
        result = controllerTransactions.getAllPassTrs(account_num, connection, cursor)

        if result:
         
           print ("\nPlease, find below all your pass transactions \n")
         
           controllerTransactions.printAllTrs(result, connection, cursor)

        else:
           print("\nThere no transaction line found!\n Please check and try again later! \n")


    #view all transactions
    if choice == 8:

        controllerTransactions = ControllerTransactions.Functionalities()
        result = controllerTransactions.getAllTrs(connection, cursor)

        if result:
           print ("\nPlease, below the list of all transactions \n")

           controllerTransactions.printAllTrs(result, connection, cursor)

        else:
           print("\nThere no transaction line found!\n Please check and try again later! \n")










 
