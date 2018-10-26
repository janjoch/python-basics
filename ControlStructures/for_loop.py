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
Created on Wed Apr 19 14:44:06 2017

Descripton: 
    
"""
###############################################################################
###############################################################################


if __name__ == "__main__":

    try:
        
        #Basic for loop
        for item in [1,3,6,2,5]:
            print("Item Nr.:", item)
            
        #Plot of sinus signal with different Amplitude          
        x = np.arange(0, 4*np.pi, 0.1);        
        for A in range(1,4):  
            y = A*np.sin(x)
            plt.plot(x, y)
            plt.legend([1,2,3])
            plt.ylim([-4,4])
            plt.xlabel("x axis")
            plt.ylabel("y axis")
            plt.title("Sinus wave with different amplitudes")
            
        
    except:
        traceback.print_exc()



