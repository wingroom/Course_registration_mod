import tkinter as tk
from tkinter import ttk
import os
import sys
import Course_registration_FILE as FILE

class main_gui(tk.Frame):
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath('.'), relative_path)

    def __init__(self, master,jf):
        super().__init__(master)
        self.pack()
        master.geometry('1000x620')
        master.title('履修')
        master.iconbitmap(self.resource_path('icon.ico'))
        self.sum=0
        self.jf=jf
        self.subwin=None
        self.main_gui()
    
    def main_gui(self):
        self.semecsv=FILE.csv_reader8(f'all\{self.jf["semester"]}.csv')
        self.countlist=[]
        for i in range(1,5):
            for j in range(1,5):
                self.countlist.append('B'+str(i)+' '+str(j)+'Q')
        self.semester=tk.StringVar(self)
        self.semester.set(' '.join(self.jf["semester"].split('_')))
        self.semem=tk.OptionMenu(self,self.semester,*self.countlist,command=self.seme_sele)
        self.semem.grid(row=0,column=0)
        timetable=[[''for i in range(6)]for j in range(5)]
        for i in range(5):
            label=tk.Label(self,text=str(i+1)+'限')
            label.grid(row=i+1,column=0)
        label=tk.Label(self,text='月曜').grid(row=0,column=1)
        label=tk.Label(self,text='火曜').grid(row=0,column=2)
        label=tk.Label(self,text='水曜').grid(row=0,column=3)
        label=tk.Label(self,text='木曜').grid(row=0,column=4)
        label=tk.Label(self,text='金曜').grid(row=0,column=5)
        label=tk.Label(self,text='土曜').grid(row=0,column=6)
        for row in self.semecsv:
            if len(row):
                if ' ' in row[1]:
                    vals=row[1].split()
                else:
                    vals=[row[1],'']
                for val in vals:
                    if len(val):
                        if val[0]=='月':
                            timetable[int(val[1])-1][0]=row[0]+'\n'+row[3]
                        elif val[0]=='火':
                            timetable[int(val[1])-1][1]=row[0]+'\n'+row[3]
                        elif val[0]=='水':
                            timetable[int(val[1])-1][2]=row[0]+'\n'+row[3]
                        elif val[0]=='木':
                            timetable[int(val[1])-1][3]=row[0]+'\n'+row[3]
                        elif val[0]=='金':
                            timetable[int(val[1])-1][4]=row[0]+'\n'+row[3]
                        elif val[0]=='土':
                            timetable[int(val[1])-1][5]=row[0]+'\n'+row[3]

        for i in range(5):
            for j in range(6):
                button=tk.Button(self,text=timetable[i][j],width=20,height=7,justify=tk.CENTER,relief=tk.RIDGE)
                button.config(command=self.outer(i,j))
                button.grid(row=i+1,column=j+1)
        
    def outer(self,i,j):
        def inner():
            self.puti(time=str(j+1)+str(i+1))
        return inner

    def puti(self,time):
        #ここでサブの画面を表示させてtreeviewを使って考えよう
        csvs=FILE.csv_reader8(f'semester\{self.jf["semester"]}')
        print('puti in')
        tmp=None
        if time[0]=='1':
            tmp='月'+time[1]
        elif time[0]=='2':
            tmp='火'+time[1]
        elif time[0]=='3':
            tmp='水'+time[1]
        elif time[0]=='4':
            tmp='木'+time[1]
        elif time[0]=='5':
            tmp='金'+time[1]
        elif time[0]=='6':
            tmp='土'+time[1]
        selist=[]
        for row in csvs:
            if row[1]==tmp[0] and row[2]==tmp[1]:
                if row[3][0]=='前':
                    if row[3][-1]=='期':
                        a=5
                    elif row[3][-1]=='前':
                        a=1
                    elif row[3][-1]=='後':
                        a=2
                elif row[3][0]=='後':
                    if row[3][-1]=='期':
                        a=7
                    elif row[3][-1]=='前':
                        a=3
                    elif row[3][-1]=='後':
                        a=4
                if self.jf["semester"][3]==str(a) or (a>4 and (self.jf["semester"][3]==str(a-4) or self.jf["semester"][3]==str(a-3))):
                    if int(self.jf["semester"][1])>=int(row[4]):
                        selist.append(row)
        if self.subwin!=None:
            if self.subwin.winfo_exists():
                self.subwin.destroy()
        if self.subwin==None or not self.subwin.winfo_exists():
            self.subwin=tk.Toplevel()
            self.subwin.title(tmp)
            self.subwin.iconbitmap(self.resource_path('icon.ico'))
            self.subwin.geometry('500x400')
            self.tree=ttk.Treeview(self.subwin,selectmode=tk.BROWSE)
            self.tree['columns']=('単位名','クラス','対象','教室')
            self.tree.column('#0',width=0,stretch=False)
            self.tree.column('単位名',anchor='w',width=220)
            self.tree.column('クラス',anchor='w',width=60)
            self.tree.column('対象',anchor='w',width=120)
            self.tree.column('教室',anchor='w',width=0,stretch=False)
            self.tree.heading('#0',text='Label',anchor='w')
            self.tree.heading('単位名',text='単位名',anchor='center')
            self.tree.heading('クラス',text='クラス',anchor='center')
            self.tree.heading('対象',text='学年',anchor='center')
            self.tree.heading('教室',text='教室',anchor='w')
            for row in selist:
                if len(row)!=0:
                    self.tree.insert(parent='',index='end',values=(row[6],row[5],row[4],row[9]))
            self.tree.pack()
            self.button=tk.Button(self.subwin, text='決定',command=lambda:self.pbutton(val=[self.tree.item(self.tree.selection(), 'values'),tmp]))
            self.button.pack()

    def pbutton(self, val):
        #val [選択要素(単位名,クラス,学年,教室), 曜日]
        seme=FILE.csv_reader8(f'all\{self.jf["semester"]}.csv')
        seme.append([val[0][0],val[1],val[0][3]])
        FILE.csv_writer8(f'all\{self.jf["semester"]}.csv')
        
    def seme_sele(self,val):
        self.jf["semester"]=val
        self.main_gui()

class setup_gui(tk.Frame):
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath('.'), relative_path)

    def __init__(self, master, jf):
        super.__init__(master)
        self.pack()
        master.geometry('300x200')
        master.title('初期設定')
        master.iconbitmap(self.resource_path('icon.ico'))
        self.jf=jf
        self.setup_gui()
        
    def setup_gui(self):
        pass