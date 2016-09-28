
import csv

f1 = open('list1.csv', 'r')
f2 = open('list2.csv', 'r')
f3 = open('list3.csv', 'w',newline='')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(c2)

for hosts_row in c1:
    row = 1
    found = False
    for master_row in masterlist:
        results_row = hosts_row
        if hosts_row[0] == master_row[0]:
            
            found = True
            break
        row = row + 1
    if not found:
        results_row.append('NOT FOUND in master list')
    c3.writerow(results_row)

f1.close()
f2.close()
f3.close()
