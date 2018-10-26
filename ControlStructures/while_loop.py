# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']
"""
Created on Wed Apr 19 15:05:08 2017

Descripton: 
    
"""
###############################################################################
###############################################################################


if __name__ == "__main__":

    try:
        
        #Basic while loop
        print("Counting up to 5:")
        counter = 1
        while counter <= 5:
            print(counter)
            counter = counter + 1
        
        
        #While loop with input
        answer = input("Was it counted right? Please answer with yes or no (y/n): ")

        while answer not in ['y', 'Y', 'n', 'N']:
            
            print('Invalid answer!')
            answer = input("Please answer with yes orn no (y/n): ")
                
        print("Thank you!")
        
    except:
        traceback.print_exc()