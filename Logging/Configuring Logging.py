# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import time
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
Created on Mon Sep 24 10:49:13 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        
        # create logger
        logger = logging.getLogger("Loger_example")
        logger.setLevel(logging.DEBUG)
        
        # create log file handler and set level to debug
        log_file = logging.FileHandler("config_log.log")
        log_file.setLevel(logging.DEBUG)
        
        # create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        
        # add formatter to ch
        log_file.setFormatter(formatter)
        
        # add ch to logger
        logger.addHandler(log_file)
        
        # application code
        logger.debug("debug message")
        time.sleep(2)
        logger.info("info message")
        logger.warning("warn message")
        time.sleep(5)
        logger.error("error message")
        logger.critical("critical message")
                
        
    except:
        traceback.print_exc()
