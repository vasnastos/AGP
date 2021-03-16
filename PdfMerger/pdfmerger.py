from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyPDF2 import PdfFileMerger,PdfFileReader,PdfFileWriter
import os
import re
import webbrowser as wb
#https://realpython.com/pdf-python/
#pip install pyPdf


def copy(filename,merger):
   pdf=PdfFileReader(filename)
   for x in range(pdf.numPages):
       merger.addPage(pdf.getPage(int(x))) 

def info(filename):
    reader=PdfFileReader(filename)
    information=reader.getDocumentInfo()
    return f"""
    Information about:{filename}
    Author:{information.author}
    Creator:{information.creator}
    Subject:{information.subject}
    Title:{information.title}
    Pages:{reader.numPages}
    """

def main():
    files=[x for x in os.listdir('.') if re.match('.*\.pdf',x)]
    print('Pdf''s Info')
    print('*************************************')
    for k in files:
        print(info(k))
    print('\nMerged File Creation in progrees!!!')
    name=input('Give filename:')
    if re.match('.*\.pdf',name):
        pass
    else:
        name+='.pdf'
    writer=PdfFileWriter()
    for k in files:
        copy(k,writer)
    with open(name,'wb') as f:
        writer.write(f)
    print('file created as:'+os.getcwd()+'\\'+str(name))
    l=input('Open the merged pdf(y/n):')
    if l.upper()=='Y':
      url=os.getcwd()+'\\'+str(name)
      wb.open_new_tab(url)

main()