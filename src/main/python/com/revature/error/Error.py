#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Error
#By Bertrick


class Error(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

