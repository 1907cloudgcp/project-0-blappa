#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Users class
#By Bertrick

import logging

class Users:
	
    def __init__(self, name, email, phnumber, birth_date, username, pswd, createdAt, updatedAt, enabled):

         self.name          = name

         self.email         = email

         self.phnumber      = phnumber

         self.birth_date    = birth_date

         self.username      = username

         self.pswd          = pswd

         self.createdAt     = createdAt

	 self.updatedAt     = updatedAt

	 self.enabled       = enabled
