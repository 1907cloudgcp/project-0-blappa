#!/usr/bin/env python3
#By Bertrick

import logging
from service import Services
from controller import Controller

'''
This is your main script, this should call several other scripts within your packages.
'''

def run_app(connection, cursor, functions):

	    message = '''
		----- WELCOME TO BANK P0 -------- \n 
		Please, enter parameters of connection 
		'''

            print(message)

	    #parameter of user
            username = raw_input("Login : ")
	    pswd  = raw_input("Password : ")
	    
	    #check user
	    if(functions.login(username, pswd, connection, cursor)):
	        functions.show_menu(connection, cursor)
	    else:
	        print("\nUsername or Password incorect, \nPlease try again later!\n")



def main():

	#get connection to database
        utilities = Services.DATAUtilities()
	con = utilities.getConnection()
        
        connection = con[0]        
        cursor = con[1]
        
        #get all functionalities
        functions = Controller.Functionalities()

        run_app(connection, cursor, functions)
        
        #close connection database
        connection.close()


if __name__ == '__main__':
	main()
