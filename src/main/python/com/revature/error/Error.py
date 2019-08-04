#-*- coding: utf-8 -*-
#!/usr/bin/env python3
#Error
#By Bertrick


class MyError(Exception):
    def __init__(self, message, animal):
        self.message = message
        self.animal = animal
    def __str__(self):
        return self.message
