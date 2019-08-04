#!/usr/bin/env python3
#By Bertrick

'''
This is your script to get connexion to Data Base.
'''

import logging
import mysql.connector
from mysql.connector import Error



class DATAMySQL:


	def getConnection(self):
		try:
			connection = mysql.connector.connect(host='localhost',database='bank_p0',user='root', password='')
			if connection.is_connected():
				db_Info = connection.get_server_info()
				cursor = connection.cursor()
				cursor.execute("select database();")
				record = cursor.fetchone()
				message = "Connected to MySQL database..."
		except Error as e :
				message = "Error while connecting to MySQL" + e

		return [connection, cursor, message]



class DATAPostgreSQL:
      
     def getConnection(self):

         return


class DATASQLlite:

      def getConnection(self):

         return
