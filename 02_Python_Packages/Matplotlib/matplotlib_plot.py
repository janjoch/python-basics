# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
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
Created on Thu Nov  8 14:28:03 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        
        #Generate dummy data
        x = np.linspace(0,20,1000)
        y = np.sin(x)
        yy = np.cos(x)
        
        #Plot data
        plt.figure()
        plt.plot(x,y)
        plt.plot(x,yy)
        plt.legend(["sinus", "cosinus"])
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.title("Sinuns and cosinus plot")
        
    except:
        traceback.print_exc()
