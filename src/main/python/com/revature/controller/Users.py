#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Users class
#By Bertrick

import logging

class Users():
	
    def __init__(self, name, email, number, login, pswd, status):
      self.name = name
      self.email = email
      self.number = number
      self.login = login
      self.pswd = pswd
      self.status = status