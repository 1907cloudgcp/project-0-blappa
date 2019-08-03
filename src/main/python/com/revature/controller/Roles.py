#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Roles
#By Bertrick

import logging


class Roles:
    
    def __init__(self, name, description, createdAt, updatedAt, enabled):

           self.name        = name

           self.description = description

           self.createdAt   = createdAt

           self.updatedAt   = updatedAt

           self.enabled     = enabled
