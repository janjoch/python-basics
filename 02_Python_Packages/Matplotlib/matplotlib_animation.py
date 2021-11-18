# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("../plot_style.mplstyle")
from matplotlib.animation import FuncAnimation
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Fri Nov  9 15:47:56 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        #Create dummy data
        x = np.linspace(0, 2*np.pi, 128)
        y = np.sin(x)
        
        #Prepare fix plot
        fig, ax = plt.subplots()
        plt.plot(x, y)
        xdata, ydata = [], []
        ln, = plt.plot([], [], 'ro', animated=True)
        lm, = plt.plot([], [], 'green', animated=True)
        
        #Define initial limits of plot
        def init():
            ax.set_xlim(0, 2*np.pi)
            ax.set_ylim(-1.2, 1.2)
            return ln, lm,
        
        #Define update function
        def update(frame):
            xdata.append(frame)
            ydata.append(np.sin(frame))
            ln.set_data(xdata, ydata)
            lm.set_data(frame + np.linspace(0,0,5), np.linspace(0, np.sin(frame), 5))
            return ln, lm,
        
        #Create animation
        ani = FuncAnimation(fig, update, frames=x,
                            init_func=init, blit=True)
                
    except:
        traceback.print_exc()
