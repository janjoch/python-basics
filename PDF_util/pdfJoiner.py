## -*- coding: utf-8 -*-
###############################################################################
#
# Import section
###############################################################################
import traceback
import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
###############################################################################
#
# Header
###############################################################################
__author__ = ['Marco Jordi']
__maintainer__ = ['Marco Jordi']
__email__ = ['mail.mjordi@gmail.com']
"""
Created on Tue Nov 13 19:58:55 2018

Descripton: 
    
"""
###############################################################################
###############################################################################

def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
 
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == "__main__":

    try:
        
        paths = glob.glob('C:/Users/Marco Jordi/Desktop/pdfUtilities/*.pdf')
        paths.sort()
        merger('merged.pdf', paths)
            
    except:
        traceback.print_exc()

