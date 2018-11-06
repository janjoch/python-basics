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
Created on Tue Nov  6 15:30:14 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        #Integer
        a = 32
        b = a + 2
        print("a is: ", type(a))
        print("b is: ", type(b))
        
        #Float
        c = b - 0.2
        print("c is: ", type(c))
        
        #Complex numbers
        d = 2+3j
        print("d is: ", type(d))
        
        #Strings
        s = "I am a string. "
        st = s + "And a second string"
        print(st)
        print(type(st))
        
        #Boolean (True or False)
        e = True
        print("e is: ", type(e))
        
        #List - ordered sequence of items (mutable)
        l = [1, 2, 3, 4, 5, "python"]
        print("l is: ", type(l))
        
        #Tuple - ordered sequence of items (immutable)
        t = (5,'program', 1+3j)
        print("t is: ", type(t))
        
        #Dictionary - unordered collection of key-value pairs (optimized for retrieving data)
        f = {1:'value','key':2}
        print("f is: ", type(f))
        
        """
        For morre informations see:
        https://realpython.com/python-data-types/
        https://www.programiz.com/python-programming/variables-datatypes
        """
        
    except:
        traceback.print_exc()
