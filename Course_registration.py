import os
import sys
#import tkinter as tk
#import Course_registration_GUI as GUI
import Course_registration_PDF as PDF

#GUIとpdfとseleniumで分ける

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

def main():
    #root=tk.Tk()
    #gui = GUI.gui(master=root)
    #gui.mainloop()
    PDF.pdf('semester.pdf')
    

if __name__=='__main__':
    main()