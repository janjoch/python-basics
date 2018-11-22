# -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
from PyPDF2 import PdfFileWriter, PdfFileReader
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['marco.jordi@bfh.ch']

"""
Created on Wed Nov 14 07:35:37 2018

@author: Marco Jordi
"""
###############################################################################
###############################################################################
class pdf_GUI:
    
    def __init__(self, master, img):
        """Initialize the GUI - Pdf util
    
        Args:
            :master: Root of TKInter object
        """ 
        #Settings for GUI
        self.master = master
        self.master.geometry("600x275+400+200")
        self.master.wm_title("PDF merger")
        self.master.configure(background="white", )
        self.font1 = Font(family="Calibri", size=16, weight="bold")
        self.font2 = Font(family="Calibri", size=12)
        self.font3 = Font(family="Calibri", size=8)
        
        #Insert pdf icon
        logo = tk.Canvas(self.master, width=100, height=80, bd=0, bg="white",
                            highlightthickness=0)
        logo.grid(row=0, column=2, columnspan=1, padx=(0, 0))
        logo.create_image(0,10, anchor=tk.NW, image=img)
                          
        #Create Caption Text
        self.create_text("PDF merger", self.font1, 
                         height=1, width=12, row=0, column=0, columnspan=1)
        self.create_text("Input pdf file 1:", self.font2, 
                         height=0, width=15, row=2, column=0, columnspan=1)
        self.create_text("Input pdf file 2:", self.font2, 
                         height=0, width=15, row=3, column=0, columnspan=1)
        self.create_text("Output file name:", self.font2, 
                         height=0, width=15, row=4, column=0, columnspan=1)
        self.create_text("Developed by marco jordi:", self.font3, 
                         height=0, width=76, row=6, column=0, columnspan=2)
        #Create Buttons
        self.button0 = tk.Button(self.master, text="Browse File", 
                                 command=self.select_file1, width=15)
        self.button0.grid(row=2, column=2, padx=(1, 1), pady=(5, 5))
        self.button1 = tk.Button(self.master, text="Browse File", 
                                 command=self.select_file2, width=15)
        self.button1.grid(row=3, column=2, padx=(1, 1), pady=(5, 5))
        self.button2 = tk.Button(self.master, text="Merge PDF's", 
                                 command=self.merger, width=15)
        self.button2.grid(row=5, column=0, padx=(1, 1), pady=(20, 23))
        
        #Insert Lines
        self.create_horline(width=600, height=10, row=1, column=0, rowspan=1, 
                            columnspan=3)

        #Entry widgets
        self.e0 = tk.Entry(self.master, width=50)
        self.e0.grid(row=2, column=1, padx=(1, 1), pady=(5, 5))
        self.e1 = tk.Entry(self.master, width=50)
        self.e1.grid(row=3, column=1, padx=(1, 1), pady=(5, 5))
        self.e2 = tk.Entry(self.master, width=50)
        self.e2.grid(row=4, column=1, padx=(1, 1), pady=(5, 5))

            
    def create_text(self, text, font, height, width, row, column, columnspan=1):
            """Creates a text in the GUI
        
            Args:
                :text: String of the text which should show up
                :font: Text font
                :height: Height of the text
                :width: Width of the text
                :row: Row, where the text should be placed in the grid of the GUI
                :column: Column, where the text should be placed in the grid of the GUI
                :columnspan: Over how many columns the text should span (default = 1)
            """ 
            tktext= tk.Text(self.master, height=height, width=width, bd=0)
            tktext.grid(row=row, column=column, columnspan=columnspan)
            tktext.insert(tk.INSERT, text)
            tktext.configure(font=font)
            
    def create_horline(self, width, height, row, column, rowspan=1, columnspan=1):
        """Creates a horizontal line in the GUI
    
        Args:
            :width: Width of the line
            :height: Height of the line
            :row: Row, where the line should be placed in the grid of the GUI
            :column: Column, where the line should be placed in the grid of the GUI
            :rowspan: Over how many columns the line should span (default = 1)
            :columnspan: Over how many columns the line should span (default = 1)
        """ 
        
        line0 = tk.Canvas(self.master, width=width, height=height, bg="white",
                          highlightthickness=0)
        line0.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
        line0.create_line(0, 5, width, 5, fill="#476042")
    
    def merger(self):
        """Merge two pdf files to one
        """ 
        input_paths = [self.input_path1, self.input_path2]
        output_path = self.e2.get()+".pdf"
        
        pdf_writer = PdfFileWriter()
     
        for path in input_paths:
            pdf_reader = PdfFileReader(path)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
     
        with open(output_path, 'wb') as fh:
            pdf_writer.write(fh)
    
    def select_file1(self):
        """Browse for pdf file 1 and choose it
        """
        self.input_path1 = filedialog.askopenfilename(title = "Select file",
                                                      filetypes = [('pdf file', '*.pdf')])
        self.e0.insert(0, self.input_path1)
        
    def select_file2(self):
        """Browse for pdf file 2 and choose it
        """
        self.input_path2 = filedialog.askopenfilename(title = "Select file",
                                                      filetypes = [('pdf file', '*.pdf')])
        self.e1.insert(0, self.input_path2)
            
    
        
###############################################################################

if __name__ == "__main__":

    try:
        
        #Initialize GUI
        root = tk.Tk()
        img = tk.PhotoImage(file="pdf_icon.gif")
     
        #Starting GUI
        app = pdf_GUI(root, img)
        root.mainloop()
        
        
    except:
        traceback.print_exc()
