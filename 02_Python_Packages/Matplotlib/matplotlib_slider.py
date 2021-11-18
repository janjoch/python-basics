# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("../plot_style.mplstyle")
from matplotlib.widgets import Slider, Button, RadioButtons
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Thu Nov  8 14:52:16 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################

def update(val):
    """
    Update figure when amplitude or frequency is changed
    """
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
    
def reset(event):
    """Reset figure to standard values
    """
    sfreq.reset()
    samp.reset()
    
def colorfunc(label):
    """Change color of graph
    """
    l.set_color(label)
    fig.canvas.draw_idle()


if __name__ == "__main__":

    try:
        
        #Create data
        t = np.arange(0.0, 1.0, 0.001)  #time
        a0 = 5                          #Amplitude
        f0 = 3                          #frequence
        s = a0*np.sin(2*np.pi*f0*t)     #sinus signal
        
        #Plot data
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        l, = plt.plot(t, s, lw=2, color='red')
        plt.axis([0, 1, -10, 10])
        
        #Create slider axes
        axcolor = 'whitesmoke'
        delta_f = 5.0
        axfreq = plt.axes([0.19, 0.1, 0.65, 0.03], facecolor=axcolor)
        axamp = plt.axes([0.19, 0.15, 0.65, 0.03], facecolor=axcolor)
        sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
        samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
        
        #Update plot when amplitude or frequency is changed
        sfreq.on_changed(update)
        samp.on_changed(update)
        
        #Create reset button
        resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
        button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
        button.on_clicked(reset)
        
        #Create legendbox to change color of the graph
        rax = plt.axes([0.815, 0.75, 0.08, 0.12], facecolor=axcolor)
        radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
        radio.on_clicked(colorfunc)
        
        
    except:
        traceback.print_exc()
