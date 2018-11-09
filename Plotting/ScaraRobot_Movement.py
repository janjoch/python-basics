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
        p1 = np.linspace((-phi1/180)*np.pi, (phi1/180)*np.pi, 1000)
        p2 = np.linspace(0, (phi2/180)*np.pi, 1000)
        p22 = np.linspace(-(phi2/180)*np.pi, (phi2/180)*np.pi, 1000)
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
        for p1i in p1:
            for p2i in p22:
                xx.append(r1 * np.cos(p1i) + r2 * np.cos(p1i + p2i))
                yy.append(r1 * np.sin(p1i) + r2 * np.sin(p1i + p2i))
        
        #Plot figure
        plt.figure(figsize=(8,6))
        plt.plot(x1,y1,x2,y2,x3,y3, lw=3)
        plt.plot(xx, yy,alpha=0.3)
        plt.plot(cross, 0*cross, lw=0.5, color="black")
        plt.plot(0*cross, cross, lw=0.5, color="black")
        plt.legend(["Fall 1","Fall 2","Fall 3","Gesamt",])
        plt.title("Scara Roboter Arbeitsbereich")
        plt.xlabel("X-Achse")
        plt.xlabel("Y-Achse")
        plt.axis('equal')
    
    
    except:
        traceback.print_exc()
