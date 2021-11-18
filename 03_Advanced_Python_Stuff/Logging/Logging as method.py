# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import logging
import traceback
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("../plot_style.mplstyle")
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Mon Sep 24 10:37:42 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################

def log_main():
    """Creates log file with info of starting and finishing time
    
    """
    #create logger
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
    
    # application
    logger.info("Started with plot")
    
    create_plot()
    
    logger.info("Finished with plot")
    

def create_plot():
    """Creates a basic plot
    
    """
    x = np.arange(0,10,0.01)
    y = np.sin(x)
    
    plt.figure()
    plt.plot(x,y)


if __name__ == "__main__":

    try:
        
        log_main()
        
    except:
        traceback.print_exc()
