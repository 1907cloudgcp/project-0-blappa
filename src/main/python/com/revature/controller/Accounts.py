#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Accounts
#By Bertrick

import logging

class Accounts:

    def __init__(self, account_name, account_num, typeA, description, createdAt, updatedAt, enabled):

		self.account_name = account_name

		self.account_num  = account_num

		self.typeA        = typeA

		self.description  = description

		self.createdAt    = createdAt

		self.updatedAt    = updatedAt

		self.enabled      = enabled
