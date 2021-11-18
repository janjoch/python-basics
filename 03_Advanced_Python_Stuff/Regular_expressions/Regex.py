# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import re
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Tue Nov 20 14:27:53 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        #Regular Expressions
        #match function
        word = input("Enter a word: ")
        p1 = re.match("[A-Za-z]", word, flags=0)
        
        print("\nChecking with match!")
        while p1 == None:
            print("This is no word! Please enter a word with char [A-Z] or [a-z]!")
            word = input()
            p1 = re.match("[A-Za-z]", word, flags=0)
            
        #Group
        print("This is a word!")
        
        #Match vs search (match checks for a match only at the beginning of the
        #string, while search checks for a match anywhere in the string)
        word = input("Enter a word: ")
        p2 = re.search("[A-Za-z]", word, flags=0)
        
        print("\nChecking with search!")
        while p1 == None:
            print("This is no word! Please enter a word with char [A-Z] or [a-z]!")
            word = input()
            p1 = re.search("[A-Za-z]", word, flags=0)
        print("Thank you!")
            
    except:
        traceback.print_exc()
