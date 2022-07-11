from asyncio.windows_events import NULL
import tkinter as tk
import Course_registration_GUI as GUI
import Course_registration_PDF as PDF
import Course_registration_FILE as FILE

#GUIとpdfとseleniumで分ける
def tmp():
    PDF.semepdf('semester.pdf')
    print('finish')

def main():
    json_file = FILE.json_reader("setup.json")
    if json_file["Department"]==NULL:
        root=tk.Tk()
        gui=GUI.setup_gui(master=root, jf=json_file)
        gui.mainloop()
    if json_file["Department"]!=NULL:
        root=tk.Tk()
        gui=GUI.main_gui(master=root, jf=json_file)
        gui.mainloop()

if __name__=='__main__':
    tmp()