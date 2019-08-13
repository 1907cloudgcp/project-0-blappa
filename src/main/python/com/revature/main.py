#!/usr/bin/env python3
#By Bertrick

import logging
import menu
from controller import UsersController
from tool import Drivers


'''
This is your main script, this should call several other scripts within your packages.
'''

def run_app(connection, cursor):
          
            logging.basicConfig(filename='../../../resources/app.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

	    message = '''
		------->>> WELCOME TO BANK PROJET 0 \n
		Please, enter your login and password to connect 
		'''

            print(message)

	    #parameter of user
            username = raw_input("Login : ")
	    pswd  = raw_input("Password : ")
	    
	    #check and connect user
            userController = UsersController.Functionalities()
  
            #get current user
            name = userController.login(username, pswd, connection, cursor)            
            
	    if name:
               #welcome messsage
               print("\n Hey, welcome %s \n" % (name))

               logging.info('User %s login successuful' , name)
           
               result = 1
               while result == 1:
	           menu.show_menu(connection, cursor)
                   result = input("Press 1 to continue Or 0 to exit \n")

	       print("\n----- GoodBye %s !!\n" % (name))

            else:
	        print("\nUsername or Password incorect, \nPlease try again later!\n")
                logging.warning('Username or Password incorect, \nPlease try again later!')                
 
            #close connection to database
            userController.logout(connection, cursor)  


def main():

        #get driver mysql conection
        mysql = Drivers.DATAMySQL()
	
        #get connection to mysql database
        con = mysql.getConnection()
        
        connection = con[0]        
        cursor = con[1]

        run_app(connection, cursor)


if __name__ == '__main__':
	main()
