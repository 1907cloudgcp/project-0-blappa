#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Transactions
#By Bertrick

import logging


class Transactions:
    
    def __init__(self, name, description, typeTrs, creation_date, startDate, endDate, createdAt, updatedAt, enabled):

		   self.name          = name

		   self.description   = description

		   self.typeTrs       = typeTrs

		   self.creation_date = creation_date

		   self.startDate     = startDate

		   self.endDate       = endDate

		   self.createdAt     = createdAt

		   self.updatedAt     = updatedAt

		   self.enabled       = enabled
