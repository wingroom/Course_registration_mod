import csv
import json
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)

def csv_reader8(file_path):
    with open(resource_path(file_path),newline='',encoding='utf-8-sig') as f:
        reader=csv.reader(f)
        a=[row for row in reader]
    return a

def csv_reader(file_path):
    with open(resource_path(file_path), newline='') as f:
        reader=csv.reader(f)
        a=[row for row in reader]
    return a

def csv_writer8(file_path,val):
    with open(resource_path(file_path),'w',newline='',encoding='utf-8-sig') as f:
        writer=csv.writer(f)
        writer.writerows(val)

def csv_writer8_a(file_path, val):
    with open(resource_path(file_path), 'a', newline='', encoding='utf-8-sig') as f:
        writer=csv.writer(f)
        writer.writerow(val)

def json_reader(file_path):
    with open(resource_path(file_path),'r') as f:
        val=json.load(f)
    return val

def json_writer(file_path,val):
    with open(resource_path(file_path),'w') as f:
        json.dump(val,f,indent=4)