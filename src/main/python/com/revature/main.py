#!/usr/bin/env python3
#By Bertrick

import logging
from service import Services

'''
This is your main script, this should call several other scripts within your packages.
'''
def main():
        utilities = Services.DATAUtilities()
	con = utilities.getConnection()
        
        connection = con[0]        
        cursor = con[1]

        cursor.execute("SELECT * FROM users")

        myresult = cursor.fetchall()
        
        for x in myresult:
           print(x) 
    
        connection.close()


if __name__ == '__main__':
	main()
