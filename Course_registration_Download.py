import re
import requests
from bs4 import BeautifulSoup as bs
import Course_registration_FUNC as FUNK
import Course_registration_FILE as FILE

def Download():
    print('link_in')
    res=requests.get('https://www.asc.tcu.ac.jp/')
    res.raise_for_status()
    soup=bs(res.text, "html.parser")
    elem=soup.find("a", text='授業時間表')
    print(elem.attrs['href']+' , '+elem.contents[0])
    res=requests.get(elem.attrs['href'])
    res.raise_for_status()
    soup=bs(res.text, "html.parser")
    Department=FUNK.departmentjunp(FILE.json_reader('setup\setup.json')['Department'][2:4])
    print(Department)
    elems=soup.find_all("a", text=Department, limit=2)
    print(elems)
    #ここで一つ目と二つ目を開きたい
    for i in range(len(elems)):
        print('書き込み'+str(i+1)+'回目')
        with open(f'setup\seme{i+1}.pdf', mode='wb') as f:
            f.write(requests.get(elems[i].attrs['href']).content)
    elems=soup.find_all("a", text=re.compile('授業時間表変更一覧'), limit=2)
    print(elems)
    for i in range(len(elems)):
        with open(f'setup\seme_change{i+1}.pdf', mode='wb') as f:
            f.write(requests.get(elems[i].attrs['href']).content)