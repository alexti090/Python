import pandas as pd
import csv

rows1 = []
rows2 = []

with open("./data1.csv", 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    rows1.append(row)

with open("./data2.csv", 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    rows2.append(row)

headers = rows1[0]
data1 = rows1[1:]
data2 = rows2[1:]
temp1 = rows1[1:]
temp2 = rows2[1:]

print("\nThese values from data1 were not included:\n")
for star in temp1:
  try:
    star[0] = int(star[0])
    star[2] = float(star[2])
    star[3] = float(star[3])
    star[4] = float(star[4])
  except:
    print(star)
    data1.remove(star)

print("\nThese values from data2 were not included:\n")
for star in temp2:
  try:
    star[0] = int(star[0])
    star[2] = float(star[2])
    star[3] = float(star[3])*0.000954588
    star[4] = float(star[4])*0.102763
  except:
    print(star)
    data2.remove(star)

data = data1 + data2

with open('./merged-data.csv', 'a+')as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(data)