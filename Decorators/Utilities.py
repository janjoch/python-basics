# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
from datetime import datetime
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Mon Sep 24 11:23:00 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            print("It's not night!")
            func()
        else:
            print("It's night, please be quiet!")

    return wrapper

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

