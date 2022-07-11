from msilib.schema import File
import tabula
import Course_registration_FILE as FILE

def semepdf(pdf_path):
    tabula.convert_into(pdf_path, 'seme.csv', output_format='csv', pages='all')
    
    val=FILE.csv_reader('seme.csv')
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
        
    for i in range(4):
        for j in range(4):
            for k in range(5):
                FILE.csv_writer8(f'semester\B{i+1}_{j+1}Q\月{k+1}.csv','')
                FILE.csv_writer8(f'semester\B{i+1}_{j+1}Q\火{k+1}.csv','')
                FILE.csv_writer8(f'semester\B{i+1}_{j+1}Q\水{k+1}.csv','')
                FILE.csv_writer8(f'semester\B{i+1}_{j+1}Q\木{k+1}.csv','')
                FILE.csv_writer8(f'semester\B{i+1}_{j+1}Q\金{k+1}.csv','')
                FILE.csv_writer8(f'semester\B{i+1}_{j+1}Q\土{k+1}.csv','')
        FILE.csv_writer8(f'semester\B{i+1}\\1st.csv','')
        FILE.csv_writer8(f'semester\B{i+1}\\2nd.csv','')
    FILE.csv_writer8('semester\\all.csv','')

    for i in range(len(val)):
        if val[i][3]=='前期':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_1Q\{val[i][1]}{val[i][2]}.csv',val[i])
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_2Q\{val[i][1]}{val[i][2]}.csv',val[i])
        elif val[i][3]=='前期前':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_1Q\{val[i][1]}{val[i][2]}.csv',val[i])
        elif val[i][3]=='前期後':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_2Q\{val[i][1]}{val[i][2]}.csv',val[i])
        elif val[i][3]=='後期':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_3Q\{val[i][1]}{val[i][2]}.csv',val[i])
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_4Q\{val[i][1]}{val[i][2]}.csv',val[i])
        elif val[i][3]=='後期前':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_3Q\{val[i][1]}{val[i][2]}.csv',val[i])
        elif val[i][3]=='後期後':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}_4Q\{val[i][1]}{val[i][2]}.csv',val[i])
        elif val[i][3]=='前集中':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}\\1st.csv',val[i])
        elif val[i][3]=='後集中':
            FILE.csv_writer8_a(f'semester\B{val[i][4]}\\2nd.csv',val[i])
        elif val[i][3]=='通年':
            FILE.csv_writer8_a('semester\\all.csv',val[i])

def unitpdf(file_path):
    tabula.convert_into(file_path, 'unit.csv', output_format='csv', pages='4')