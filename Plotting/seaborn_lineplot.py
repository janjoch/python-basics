# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Thu Aug 16 16:04:15 2018

@author: Marco Jordi
"""
###############################################################################
################################################################################ -*- coding: utf-8 -*-
   
if __name__ == "__main__":

    try:
        
        #Generate dummy data
        rs = np.random.RandomState(365)
        values = rs.randn(365, 4).cumsum(axis=0)
        dates = pd.date_range("1 1 2016", periods=365, freq="D")
        data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
        data_mean = data.rolling(7).mean()
        
        #Define seaborn plot style
        sns.set(style="whitegrid")
        
        #Plot data with lineplot
        ax = sns.lineplot(data=data, palette="tab10", linewidth=2.5)
        ax.set(xlabel="Date", ylabel="Y-values")
        plt.show()
        
        
    except:
        traceback.print_exc()
