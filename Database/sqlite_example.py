# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import sqlite3
import traceback
import pandas as pd
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
Created on Tue Oct  2 15:22:39 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
   
if __name__ == "__main__":

    try:
        
        #Create dummy Data
        labels = pd.Series(list('abcdefghi'))
        df = pd.get_dummies(labels)
        
        #Create and connect to database
        conn = sqlite3.connect('example.db')
        
        #Write data in database
        df.to_sql(name="new_table", con=conn, if_exists="replace")    
        
        #Read data
        cursor = conn.cursor()
        querry = "SELECT d FROM new_table"
        cursor.execute(querry)
        data = pd.DataFrame(cursor.fetchall())
        
        #Plot data
        data.plot.bar()
        
    except:
        traceback.print_exc()
