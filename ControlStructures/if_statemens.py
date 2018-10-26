# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import matplotlib.pyplot as plt
plt.style.use("C:/Users/Marco Jordi/Documents/Python Scripts/jrm1.mplstyle")
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Fri Oct 26 13:09:40 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        
        value = int(input("Enter a random value: "))
        
        #Basic if else statement
        if value < 0:
            print("  Value is negative")
        else:
            print("  Value is positive")
           
        #Multiple if else statements
        if value > 100:
            print("  Value is bigger than 100")
        elif value > 50:
            print("  Value is between 50 and 100")
        elif value == 50:
            print("  Value is 50!")
        else:
            print("  Value is smaller than 50")
            
    except:
        traceback.print_exc()
