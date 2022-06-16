from __future__ import barry_as_FLUFL
import tabula
import csv

def pdf(pdf_path):
    tabula.convert_into(pdf_path, 'seme.csv', output_format='csv', pages='all')
    
    with open('seme.csv', newline='') as f:
        reader=csv.reader(f)
        val=[row for row in reader]
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
                for k in range(11,10-j,-1):
                    val[i][k]=val[i][k+j-10]
                for k in range(0,11-j):
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
                        for k in range(11, 8 - j, -1):
                            val[i][k] = val[i][j+k-8]
                        for k in range(0,11-j):
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
    with open('seme_after.csv', 'w', newline='', encoding='utf-8-sig') as  f:
        writer=csv.writer(f)
        writer.writerows(val)