from doctest import master
from logging import root
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Course_registration_FILE as FILE
import pandas as pd

class main_gui(tk.Frame):
    def __init__(self, master,jf):
        super().__init__(master)
        self.pack()
        master.geometry('1400x720')
        master.title('履修')
        master.iconbitmap(FILE.resource_path('icon.ico'))
        self.sum=0
        self.jf=jf
        self.subwin=None
        self.main_gui()

    def main_gui(self):
        menu_bar=tk.Menu(self)
        menu_setting=tk.Menu(menu_bar,tearoff=0)
        menu_bar.add_cascade(label='設定',menu=menu_setting)
        menu_setting.add_command(label='環境設定',command=self.setting)
        self.master.config(menu=menu_bar)
        self.semecsv=FILE.csv_reader8(f'all\{self.jf["semester"]}.csv')
        self.countlist=[]
        for i in range(4):
            for j in range(4):
                self.countlist.append('B'+str(i+1)+' '+str(j+1)+'Q')
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
                for i in range(len(vals)):
                    if len(vals[i]):
                        if vals[i][0]=='月':
                            timetable[int(vals[i][1])-1][0]=row[0]+'\n\n'+row[2]
                        elif vals[i][0]=='火':
                            timetable[int(vals[i][1])-1][1]=row[0]+'\n\n'+row[2]
                        elif vals[i][0]=='水':
                            timetable[int(vals[i][1])-1][2]=row[0]+'\n\n'+row[2]
                        elif vals[i][0]=='木':
                            timetable[int(vals[i][1])-1][3]=row[0]+'\n\n'+row[2]
                        elif vals[i][0]=='金':
                            timetable[int(vals[i][1])-1][4]=row[0]+'\n\n'+row[2]
                        elif vals[i][0]=='土':
                            timetable[int(vals[i][1])-1][5]=row[0]+'\n\n'+row[2]

        for i in range(5):
            for j in range(6):
                flag=False
                button=tk.Button(self,text=timetable[i][j],width=22,height=7,background='#eee',justify=tk.CENTER,relief=tk.RIDGE,font=('遊明朝',13))
                vals=FILE.csv_reader8(f'semester\{self.day(j)}{i+1}.csv')
                if not len(timetable[i][j]):
                    for row in vals:
                        if f'B{row[4]}_{self.seme(time=row[3])}Q'==self.jf["semester"] or f'B{row[4]}_{self.seme(time=row[3])-4}Q'==self.jf["semester"] or f'B{row[4]}_{self.seme(time=row[3])-3}Q'==self.jf["semester"]:
                            flag=True
                if flag:
                    button.config(background='#E8EEF6')
                button.config(command=self.outer(i=i,j=j))
                button.grid(row=i+1,column=j+1)

    def setting():
        pass

    def outer(self,i,j):
        def inner():
            self.puti(time=str(j+1)+str(i+1))
        return inner

    def puti(self,time):
        #ここでサブの画面を表示させてtreeviewを使って考えよう
        tmp=f'{self.day(int(time[0])-1)}{time[1]}'
        csvs=FILE.csv_reader8(f'semester\{tmp}.csv')
        selist=[]
        for row in csvs:
            a=self.seme(row[3])
            if self.jf["semester"][3]==str(a) or (a>4 and (self.jf["semester"][3]==str(a-4) or self.jf["semester"][3]==str(a-3))):
                if int(self.jf["semester"][1])>=int(row[4]):
                    selist.append(row)
        if self.subwin!=None:
            if self.subwin.winfo_exists():
                self.subwin.destroy()
        if self.subwin==None or not self.subwin.winfo_exists():
            self.subwin=tk.Toplevel()
            self.subwin.title(tmp)
            self.subwin.iconbitmap(FILE.resource_path('icon.ico'))
            self.subwin.geometry('500x400')
            self.tree=ttk.Treeview(self.subwin,selectmode=tk.BROWSE)
            self.tree['columns']=('単位名','クラス','対象','教室','対開講','期間')
            self.tree.column('#0',width=0,stretch=False)
            self.tree.column('単位名',anchor='w',width=220)
            self.tree.column('クラス',anchor='w',width=60)
            self.tree.column('対象',anchor='w',width=120)
            self.tree.column('教室',anchor='w',width=0,stretch=False)
            self.tree.column('対開講',anchor='w',width=0,stretch=False)
            self.tree.column('期間',anchor='w',width=0,stretch=False)
            self.tree.heading('#0',text='Label',anchor='w')
            self.tree.heading('単位名',text='単位名',anchor='center')
            self.tree.heading('クラス',text='クラス',anchor='center')
            self.tree.heading('対象',text='学年',anchor='center')
            self.tree.heading('教室',text='教室',anchor='w')
            self.tree.heading('対開講',text='対開講',anchor='w')
            self.tree.heading('期間',text='期間',anchor='w')
            for row in selist:
                if len(row)!=0:
                    self.tree.insert(parent='',index='end',values=(row[6],row[5],row[4],row[9],row[11],row[3]))
            self.tree.pack()
            self.button1=tk.Button(self.subwin, text='決定',command=lambda:self.pbutton(val=[self.tree.item(self.tree.selection(), 'values'),tmp]))
            self.button1.pack()
            self.button2=tk.Button(self.subwin,text='削除',command=lambda:self.ppbutton(time=tmp))
            self.button2.pack()

    def ppbutton(self, time):
        df=pd.read_csv(f'all\{self.jf["semester"]}.csv')
        df.drop(df[df['時間']==time].index,inplace=True)
        df.to_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig',index=False)
        self.subwin.destroy()
        self.main_gui()

    def pbutton(self, val):
        #val [選択要素(単位名,クラス,学年,教室,対開講,期間), 曜日]
        #対開講を判定したい
        seme=FILE.csv_reader8(f'all\{self.jf["semester"]}.csv')
        for i in range(len(seme)):
            if len(seme[i]):
                if seme[i][1]==val[1]:
                    df=pd.read_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig')
                    df.drop(df[df['単位名']==seme[i][0]].index,inplace=True)
                    df.to_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig',index=False)
                    if val[0][5][-1]=='期':
                        if int(self.jf["semester"][3])%2==0:
                            df=pd.read_csv(f'all\{self.jf["semester"][0:3]}{str(int(self.jf["semester"][3])-1)}Q.csv',encoding='utf-8-sig')
                            df.drop(df[df['単位名']==seme[i][0]].index,inplace=True)
                            df.to_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig',index=False)
                        else:
                            df=pd.read_csv(f'all\{self.jf["semester"][0:3]}{str(int(self.jf["semester"][3])+1)}Q.csv',encoding='utf-8-sig')
                            df.drop(df[df['単位名']==seme[i][0]].index,inplace=True)
                            df.to_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig',index=False)
                    if len(val[0][4]):
                        if val[0][4][4:6]==val[1]:
                            df=pd.read_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig')
                            df.drop(df[df['単位名']==seme[i][0]].index,inplace=True)
                            df.to_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig',index=False)
                        else:
                            df=pd.read_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig')
                            df.drop(df[df['単位名']==seme[i][0]].index,inplace=True)
                            df.to_csv(f'all\{self.jf["semester"]}.csv',encoding='utf-8-sig',index=False)
        FILE.csv_writer8_a(f'all\{self.jf["semester"]}.csv',[val[0][0], val[1],val[0][3]])
        if val[0][5][-1]=='期':
            if int(self.jf["semester"][3])%2==0:
                FILE.csv_writer8_a(f'all\{self.jf["semester"][0:3]}{str(int(self.jf["semester"][3])-1)}Q.csv',[val[0][0], val[1],val[0][3]])
            else:
                FILE.csv_writer8_a(f'all\{self.jf["semester"][0:3]}{str(int(self.jf["semester"][3])+1)}Q.csv',[val[0][0], val[1],val[0][3]])
        if len(val[0][4]):
            if val[0][4][4:6]==val[1]:
                FILE.csv_writer8_a(f'all\{self.jf["semester"]}.csv',[val[0][0], val[0][4][7:9],val[0][3]])
            else:
                FILE.csv_writer8_a(f'all\{self.jf["semester"]}.csv',[val[0][0], val[0][4][4:6],val[0][3]])
        self.subwin.destroy()
        self.main_gui()

    def seme_sele(self,val):
        self.jf["semester"]='_'.join(val.split())
        self.main_gui()

class setup_gui(tk.Frame):
    def __init__(self, master=None, jf=None):
        super().__init__(master)
        self.pack()
        self.master.geometry('250x100')
        self.master.title('初期設定')
        self.master.iconbitmap(FILE.resource_path('icon.ico'))
        self.jf=jf
        self.setup_gui()

    def setup_gui(self):
        #学籍番号と起動画面の選択
        l1=tk.Label(self,text='学籍番号上４桁')
        l2=tk.Label(self,text='起動画面')
        e1=tk.Entry(self,width=15)
        c1=ttk.Combobox(self,values=('B1','B2','B3','B4'),width=4)
        c2=ttk.Combobox(self,values=('1Q','2Q','3Q','4Q'),width=4)
        c1.set('B1')
        c2.set('1Q')
        b1=tk.Button(self,text='決定',command=lambda:self.setup(val=[e1.get(),c1.get(),c2.get()]))
        l1.grid(row=0,column=0)
        l2.grid(row=1,column=0)
        e1.grid(row=0,column=1,columnspan=2)
        c1.grid(row=1,column=1)
        c2.grid(row=1,column=2)
        b1.grid(row=2,column=1)

    def setup(self,val):
        if len(val[0])==4:
            try:
                ret=messagebox.askyesno('確認', f'学籍番号上４桁：{val[0]}\n起動画面：{val[1]} {val[2]}')
                if ret:
                    self.jf["Department"]=val[0]
                    self.jf["semester"]=val[1]+'_'+val[2]
                    FILE.json_writer('setup\setup.json', self.jf)
                    self.master.destroy()
            except:
                messagebox.showerror('エラー','学籍番号上４桁は半角数字４桁を入力してください')
        else:
            messagebox.showerror('エラー','学籍番号上４桁は半角数字４桁を入力してください')