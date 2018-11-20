# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import pandas as pd
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
Created on Tue Nov 20 09:10:40 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        
        #Create Dataframe
        df = pd.DataFrame(np.random.randn(100,4), columns=list("ABCD"))
        
        #Viewing data and describe Dataframe
        print("Head:\n", df.head())      #first 5 rows
        print("\nTail:\n", df.tail())    #last 5 rows
        print("\nDescribe:\n", df.describe()) 
        
        #Plotting
        df.plot()
        df.hist(bins=30)
        
        #Calculate Correlations
        corr_mat = df.corr()
        print("\nCorrelation Matrix:\n", corr_mat) 
        
        #Sorting
        print("\nSorted correlation values for C:\n",
              corr_mat["C"].sort_values(ascending=False))
        
    except:
        traceback.print_exc()
