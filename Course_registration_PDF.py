import tabula
import csv

def pdf(pdf_path):
    tabula.convert_into(pdf_path, 'seme.csv', output_format='csv', pages='all')
    
    with open('seme.csv', newline='') as f:
        reader=csv.reader(f)
        val=[row for row in reader]
    print(val)