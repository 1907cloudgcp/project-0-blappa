#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Users
#By Bertrick

import logging

class Users:

    def __init__(self, name, email, phnumber, birth_date, username, pswd, createdAt, updatedAt, enabled, role_id):

        self.name          = name

        self.email         = email

        self.phnumber      = phnumber

        self.birth_date    = birth_date

        self.username      = username

        self.pswd          = pswd

        self.createdAt     = createdAt

        self.updatedAt     = updatedAt

        self.enabled       = enabled

        self.role_id = role_id
