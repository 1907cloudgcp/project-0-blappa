#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Accounts
#By Bertrick

import logging

class Accounts():

    def __init__(self, acc_number, balance, creation_date, status):
      self.acc_number = acc_number
      self.balance = balance
      self.creation_date = creation_date
      self.status = status