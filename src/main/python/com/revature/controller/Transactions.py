#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Transactions
#By Bertrick

import logging


class Transactions:
    
    def __init__(self, acc_number, balance, typeTrs, creation_date, status):
    	self.acc_number = acc_number
        self.balance = balance
        self.typeTrs = typeTrs
        self.creation_date = creation_date
        self.status = status
