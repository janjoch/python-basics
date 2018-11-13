# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("../plot_style.mplstyle")
from matplotlib.animation import FuncAnimation, writers
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Fri Nov  9 13:43:40 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
        
if __name__ == "__main__":

    try:
        
        #Roboterarm Radien
        r1 = 325
        r2 = 275
        
        #Bewegungswinkel
        phi1 = 132      #Eingabe des halben Bewegungswinkel in Grad
        phi2 = 150      #Eingabe des halben Bewegungswinkel in Grad
        
        #Bewegungswinkel als Vektoren
        p1 = np.linspace((-phi1/180)*np.pi, (phi1/180)*np.pi, 100)
        p2 = np.linspace(0, (phi2/180)*np.pi, 50)
        p11 = np.linspace((-phi1/180)*np.pi, (phi1/180)*np.pi, 250)
        p22 = np.linspace(-(phi2/180)*np.pi, (phi2/180)*np.pi, 250)
        cross = np.linspace(-(r1+r2),(r1+r2))
        
        #Bewegungsgleichungen mit Fallunterscheidng
        #Fall 1: gesammter Arbeitsbereich r1
        x1 = r1 * np.cos(p1) + r2 * np.cos(p1)
        y1 = r1 * np.sin(p1) + r2 * np.sin(p1)
        #Fall 2: r1 max Winkel
        x2 = r1 * np.cos(max(p1)) + r2 * np.cos(max(p1) + p2)
        y2 = r1 * np.sin(max(p1)) + r2 * np.sin(max(p1) + p2)
        #Fall 3: r1 min Winkel
        x3 = r1 * np.cos(min(p1)) + r2 * np.cos(min(p1) - p2)
        y3 = r1 * np.sin(min(p1)) + r2 * np.sin(min(p1) - p2)
        
        #Gesamter Arbeitsbereich
        xx = []
        yy = []
        for p1i in p11:
            for p2i in p22:
                xx.append(r1 * np.cos(p1i) + r2 * np.cos(p1i + p2i))
                yy.append(r1 * np.sin(p1i) + r2 * np.sin(p1i + p2i))
        
        #Plot figure
        fig, ax = plt.subplots(figsize=(9,7))
        ax.plot(x1,y1,x2,y2,x3,y3, lw=2)
        ax.plot(xx, yy,alpha=0.15)
        ax.plot(cross, 0*cross, lw=0.5, color="black")
        ax.plot(0*cross, cross, lw=0.5, color="black")
        ax.legend(["Fall 1","Fall 2","Fall 3"])
        ax.set_title("Scara Roboter Arbeitsbereich")
        ax.set_xlabel("X-Achse")
        ax.set_ylabel("Y-Achse")
        ax.axis('equal')
        ax.set_xlim(-650, 650)
        ax.set_ylim(-650, 650)
        
        #######################################################################
        #Animation
        ln, = ax.plot([], [], 'yellowgreen', lw=6, animated=True)
        lm, = ax.plot([], [], 'green', lw=6, animated=True)
        
        #Define update function
        def update(frame):
            if frame <= 50:
                x = [r1 * np.cos(min(p1)), r1 * np.cos(min(p1)) + r2 * np.cos(min(p1)-p2[::-1][frame])]
                y = [r1 * np.sin(min(p1)), r1 * np.sin(min(p1)) + r2 * np.sin(min(p1)-p2[::-1][frame])]
                xx = [0, r1 * np.cos(min(p1))]
                yy = [0, r1 * np.sin(min(p1))]
                ln.set_data(x, y)
                lm.set_data(xx, yy)
            elif 50 < frame <= 150 :
                x = [r1 * np.cos(p1[frame-50]), r1 * np.cos(p1[frame-50]) + r2 * np.cos(p1[frame-50])]
                y = [r1 * np.sin(p1[frame-50]), r1 * np.sin(p1[frame-50]) + r2 * np.sin(p1[frame-50])]
                xx = [0, r1 * np.cos(p1[frame-50])]
                yy = [0, r1 * np.sin(p1[frame-50])]
                ln.set_data(x, y)
                lm.set_data(xx, yy)
            elif frame > 150:
                x = [r1 * np.cos(max(p1)), r1 * np.cos(max(p1)) + r2 * np.cos(max(p1)+p2[frame-150])]
                y = [r1 * np.sin(max(p1)), r1 * np.sin(max(p1)) + r2 * np.sin(max(p1)+p2[frame-150])]
                xx = [0, r1 * np.cos(max(p1))]
                yy = [0, r1 * np.sin(max(p1))]
                ln.set_data(x, y)
                lm.set_data(xx, yy)
            return ln, lm,
        
        ani = FuncAnimation(fig, update, frames=200, blit=True)
        
#        #Save figure
#        ani.save('animation.gif', writer='pillow', fps=1)
    
    except:
        traceback.print_exc()
