import csv, os
import pandas as pd

rows = []
with open("./csv-data/merged-data.csv", 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    rows.append(row)

headers = rows[0]
del headers[0]

data = rows[1:]
data2 = []

for star in data:
  try:
    star[2] = float(star[2])
    star[3] = float(star[3])
    star[4] = float(star[4])
    star[5] = float(star[5])
    del star[0]
  except:
    data.remove(star)

# 0name, 1dist, 2mass, 3radius, 4gravity

for star in data:
  if star[1] <= 100 and (150 <= star[4] <= 350):
    data2.append(star)

with open('./csv-data/temp-filtered.csv', 'a+')as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(data2)

df = pd.read_csv('./csv-data/temp-filtered.csv')
df.to_csv('./csv-data/filtered-data.csv')
os.remove('./csv-data/temp-filtered.csv')