import csv

with open('e.csv', 'w') as f:
  csvwriter = csv.writer(f)
  csvwriter.writerow([1,2,3,4])