#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Transactions
#By Bertrick

import logging


class Transactions:
    
             def __init__(self, name, description, typeTrs, startDate, endDate, createdAt, updatedAt, enabled, account_id):

		   self.name          = name

		   self.description   = description

		   self.typeTrs       = typeTrs

		   self.startDate     = startDate

		   self.endDate       = endDate

		   self.createdAt     = createdAt

		   self.updatedAt     = updatedAt
  
                   self.account_id = account_id

                   self.enabled       = enabled
