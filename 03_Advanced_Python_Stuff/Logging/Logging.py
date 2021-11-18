# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import logging
import traceback
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Mon Sep 24 10:29:39 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
               
        #Logging to a file
        logging.basicConfig(filename='config_log.log', format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')
        
        #Logging variable
        a = 2
        b = "nine"
        logging.warning("Variable a is %i and b is %s", a, b)
        
    except:
        traceback.print_exc()
