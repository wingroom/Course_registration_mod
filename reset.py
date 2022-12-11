import csv

for i in range(4):
    for j in range(4):
        with open(f'all\B{i+1}_{j+1}Q.csv','w',newline='',encoding='utf-8-sig')as f:
            writer=csv.writer(f)
            writer.writerow(['単位名','時間','教室'])