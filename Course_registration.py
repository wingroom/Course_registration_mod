import os
import sys
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFPageInterpreter

#GUIとpdfとseleniumで分ける

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

class GUI(tk.Frame):
    pass

def main():
    root=tk.Tk()
    gui = GUI(root)
    root.mainloop()


if __name__=='__main__':
    main()