#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Accounts
#By Bertrick

import logging

class Accounts:

    def __init__(self, account_name, account_num, balance, typeA, description, createdAt, updatedAt, enabled, user_id):

        self.account_name = account_name

        self.account_num  = account_num

        self.balance  = balance

        self.typeA        = typeA

        self.description  = description

        self.createdAt    = createdAt

        self.updatedAt    = updatedAt

        self.enabled      = enabled

        self.user_id= user_id
