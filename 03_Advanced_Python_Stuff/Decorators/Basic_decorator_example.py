# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
from Utilities import not_during_the_night, do_twice
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Mon Sep 24 11:05:11 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################

@not_during_the_night
def hello():
    print("Hello!")

@do_twice
def greet(name):
    print(f"Hello {name}")


if __name__ == "__main__":

    try:
        
        #basic example without parameter
        hello()
        
        #basic example with argument
        greet("Hans Rudolf, Muster")
        
    except:
        traceback.print_exc()
