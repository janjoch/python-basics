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
Created on Fri Nov 16 15:42:51 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        
        #Create dummy data
        n = 100
        x = np.linspace(0,2*np.pi,n)
        y = np.sin(x)
        
        #plot figure
        plt.figure()
        plt.plot(x,y)
        line1, = plt.plot([],[], "o", color="red")
        plt.ion()
        plt.xlim([0, max(x)])
        plt.ylim([-1.1, 1.1])
        
        #Animation
        for i in range(n):
            line1.set_data(x[i], y[i])
            plt.pause(0.1)
        
        plt.ioff()    
        plt.show()
        
        
    except:
        traceback.print_exc()
