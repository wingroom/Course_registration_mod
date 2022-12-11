import tkinter as tk
import Course_registration_GUI as GUI
import Course_registration_PDF as PDF
import Course_registration_FILE as FILE
import Course_registration_Download as Download
import reset

def tmp():
    PDF.semepdf_reset()
    PDF.semepdf('setup\seme1.pdf')
    PDF.semepdf('setup\seme2.pdf') #教養科目も検知したい
    PDF.seme_change('setup\seme_change1.pdf')
    PDF.seme_change('setup\seme_change2.pdf') #後期のものはどのように扱うか検討

def pdf():
    jf=FILE.json_reader('setup\setup.json')
    if jf["Department"]!=None:
        Download.Download() #ここで変更のファイルもダウンロードしなければならない
        PDF.semepdf_reset()
        PDF.semepdf('setup\seme1.pdf')
        PDF.semepdf('setup\seme2.pdf') #教養科目も検知したい
        PDF.seme_change('setup\seme_change1.pdf')
        PDF.seme_change('setup\seme_change2.pdf') #後期のものはどのように扱うか検討
        print('pdf_finish')
    main()

def main():
    json_file = FILE.json_reader('setup\setup.json')
    if json_file["Department"]==None:
        root=tk.Tk()
        gui=GUI.setup_gui(master=root, jf=json_file)
        gui.mainloop()
        pdf()
    else:
        root=tk.Tk()
        gui=GUI.main_gui(master=root, jf=json_file)
        gui.mainloop()

if __name__=='__main__':
    pdf()