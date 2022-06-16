import csv

def csv_reader(file_path):
    with open(file_path,newline='') as f:
        reader=csv.reader(f)
        a=[row for row in reader]
    return a

def csv_writer(file_path,val):
    with open(file_path,'w',newline='') as f:
        writer=csv.writer(f)
        writer.writerows(val)