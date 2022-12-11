import tabula
import pandas as pd
import Course_registration_FILE as FILE
import Course_registration_FUNC as FUNC

def semepdf(pdf_path):
    tabula.convert_into(pdf_path, 'setup\seme.csv', output_format='csv', pages='all')
    
    val=FILE.csv_reader('setup\seme.csv')
    for i in range(len(val)):
        try:
            if val[i][0]=='学科':
                del val[i]
        except:
            pass
    for i in range(len(val)):
        flag=False
        for j in range(11):
            if '対開講' in val[i][j+1]:
                for k in range(11,9-j,-1):
                    val[i][k]=val[i][k+j-10]
                if val[i][0]=='':
                    l=11-j
                else:
                    l=10-j
                for k in range(0,l):
                    val[i][k]=''
                flag=True
            elif '対象' in val[i][j]:
                print(str(j)+','+str(k))
                for k in range(11,9-j,-1):
                    val[i][k]=val[i][k+j-10]
                for k in range(0,10-j):
                    val[i][k]=''
                flag=True
            elif val[i][8] == '':
                try:
                    if int(val[i][j][3:]):
                        for k in range(11,7 - j, -1):
                            val[i][k] = val[i][j+k-8]
                        if val[i][0]=='' and val[i][1]!='':
                            l=9-j
                        elif val[i][0]=='':
                            l=10-j
                        else:
                            l=8-j
                        for k in range(0,l):
                            val[i][k]=''
                        flag=True
                except:
                    pass
            elif val[i][0]=='月' or val[i][0]=='火' or val[i][0]=='水' or val[i][0]=='木' or val[i][0]=='金' or val[i][0]=='土':
                for k in range(11,0,-1):
                    val[i][k]=val[i][k-1]
                val[i][0]=''
                flag=True
            if flag:
                break 
    for i in range(len(val)):
        if val[i][2]=='1' and val[i][1]=='':
            for j in range(i,i+50):
                if val[j][1]!='':
                    val[i][1]=val[j][1]
                    break
        if val[i][3]=='前期' and val[i][2]=='':
            for j in range(i,i+10):
                if val[j][2]!='':
                    val[i][2]=val[j][2]
                    break
    day=time=seme=grand=''
    for i in range(len(val)):
        if not val[i][6]=='':
            flag=False
            if not val[i][1]=='':
                day=val[i][1]
            else:
                val[i][1]=day
            if not val[i][2]=='':
                time=val[i][2]
            else:
                val[i][2]=time
            if not val[i][3]=='':
                seme=val[i][3]
            else:
                val[i][3]=seme
            if not val[i][4]=='':
                grand=val[i][4]
            else:
                val[i][4]=grand
            if val[i][3][-1]=='中' or val[i][3]=='通年':
                val[i][0]=val[i][1]=val[i][2]=''
        val[i][6]=''.join(val[i][6].splitlines())
        val[i][7]=','.join(val[i][7].splitlines())
        val[i][9]=''.join(val[i][9].splitlines())
        val[i][11]=''.join(val[i][11].splitlines())

    for i in range(len(val)):
        if val[i][3]=='前集中' or val[i][3]=='後集中' or val[i][3]=='通年':
            FILE.csv_writer8_a(f'semester\{val[i][3]}.csv',val[i])
        else:
            FILE.csv_writer8_a(f'semester\{val[i][1]}{val[i][2]}.csv',val[i])
    FILE.csv_writer8('setup\seme.csv', val)

def semepdf_reset():
    for i in range(5):
        FILE.csv_writer8(f'semester\月{i+1}.csv','')
        FILE.csv_writer8(f'semester\火{i+1}.csv','')
        FILE.csv_writer8(f'semester\水{i+1}.csv','')
        FILE.csv_writer8(f'semester\木{i+1}.csv','')
        FILE.csv_writer8(f'semester\金{i+1}.csv','')
        FILE.csv_writer8(f'semester\土{i+1}.csv','')
    FILE.csv_writer8('semester\\前集中.csv','')
    FILE.csv_writer8('semester\\後集中.csv','')
    FILE.csv_writer8('semester\\通年.csv','')

def seme_change(pdf_path):
    tabula.convert_into(pdf_path,'setup\change.csv',output_format='csv',lattice=True,pages='all')
    vals=FILE.csv_reader('setup\change.csv')
    for i in range(len(vals)):
        try:
            if vals[i][0]=='変更':
                del vals[i]
        except:
            pass
    for i in range(len(vals)):
        for j in range(len(vals[i])):
            vals[i][j]=''.join(vals[i][j].splitlines())
    dep=FUNC.departmentjunp_short(FILE.json_reader('setup\setup.json')["Department"][2:4])
    for i in range(len(vals)):
        if vals[i][8] in dep:
            for j in range(len(vals[i])):
                if '→' in vals[i][j]:
                    val=vals[i][j].split('→')
                    if j==1:
                        if val[0]=='(新規)':
                            va=vals[i][2].split('→')
                            va=va[1].split(',')
                            for v in va:
                                FILE.csv_writer8_a(f'semester\\{v}.csv',['',v[0],v[1],vals[i][2].split('→')[-1],vals[i][3].split('→')[-1],v,vals[i][4].split('→')[-1],vals[i][10].split('→')[-1],vals[i][5].split('→')[-1],vals[i][6].split('→')[-1],vals[i][7].split('→')[-1],(lambda x:'' if len(x)==1 else f'対開講({va[0]},{va[1]})',va)])
                        else:
                            val[0]=val[0].split(',')
                            for va in val[0]:
                                raw=FILE.csv_reader8(f'semester\{va}.csv')
                                for l in range(len(raw)):
                                    if raw[l][6]==vals[i][4]:
                                        v=raw[l][5]
                                        del raw[l]
                                        break
                                FILE.csv_writer8(f'semester\{va}.csv',raw)
                            if val[1]=='(削除)':
                                pass
                            else:
                                val[1]=val[1].split(',')
                                tex=''
                                if len(val[1])!=1:
                                    tex=f'対開講({val[1][0]},{val[1][1]})'
                                for va in val[1]:
                                    FILE.csv_writer8_a(f'semester\{va}.csv',['',va[0],va[1],vals[i][2].split('→')[-1],vals[i][3].split('→')[-1],v,vals[i][4].split('→')[-1],vals[i][10].split('→')[-1],vals[i][5].split('→')[-1],vals[i][6].split('→')[-1],vals[i][7].split('→')[-1],tex])
                                        #ここに対応する
                    elif j==4:
                        if val[0]=='(新規)':
                            pass
                        else:
                            allow_num=[]
                            for k in range(len(vals[i])):
                                if '→' in vals[k]:
                                    allow_num.append(k)
                            print(allow_num)

    FILE.csv_writer8('setup\change.csv',vals)

def unitpdf(file_path):
    tabula.convert_into(file_path, 'unit.csv', output_format='csv', pages='4')