#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Controller
#By Bertrick

import logging
from service import Register
from controller import Users, Accounts, Transactions



class Functionalities:

    #register = Register.Init()

    #welcome function
    def show_menu(self, connection, cursor):
        
        menu ='''
        ->> For register, press 1. \n
        ->> For view your balance, press 2.\n
        ->> For withdraw money, press 3.\n
        ->> To make deposit money, press 4. \n
        ->> To view all my past transactions, press 5
        ->> For logout, press 6. \n
        '''

        choice = int(input(menu))

        if choice == 1:
            print("Please, complete information below : \n")
            name = raw_input("Name : ")
            email = raw_input("Email : ")
            phnumber = raw_input("Phone Number : ")
            birth_date = raw_input("Birth Date : ")
            username = raw_input("Login : ")
            pswd = raw_input("Password : ")
            status = int(input("Status (enable 1 or deseable 0) "))
            user = Users(name, email, phnumber, birth_date, username, pswd, status)
                         
            result = Register.Init().create(user, connection, cursor)
            if result:
               print("\nUser saved successfully !\n Press * to continue Or 0 to exit \n")
            else:
               print("\nRegistering failure! \n")


    #login controller
    def login(self, username, pswd, connection, cursor):
  
        return Register.Init().login(username, pswd, connection, cursor)
 

    #logout controller
    def logout(self, connection, cursor):

        return 

    #deposite controller
    def deposite(self, connection, cursor):
        
        return 

    #withdraw controller
    def withdraw(self, connection, cursor):
        
        return 

    #transaction controller
    def findAllTransactions(self):
           
        return


    #ask for an ip address, using a name or MAC address
    def askIpAddr(self, name, imacAddr):
           
        return 

    #register ports with my ip address
    def registerPorts(self, ipAddr):
           
        return

    #see all ports registered to me
    def findAllPorts(self):
           
        return

    #see any traffic sent to me
    def anyTraffic(self, account):
           
        return

    #send traffic to an address.
    def sendTraffic(self, addr):
           
        return

    #send traffic to a port.
    def sendTraffic(self, port):
           
        return 

    #ports registered to them.
    def findAllAddrAndPorts(self):
           
        return

    #change any port registration
    def changeAnyPort(self, port):
           
        return







