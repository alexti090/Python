import csv

data1 = []
data2 = []

with open('./final.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    data1.append(row)

with open('./data2-sorted.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    data2.append(row)

headers1 = data1[0]
headers2 = data2[0]
planetData1 = data1[1:]
planetData2 = data2[1:]

finalHeader = headers1 + headers2
finalPlanetData = planetData1 + planetData2

with open('./final-complete.csv', 'a+')as f:
  writer = csv.writer(f)
  writer.writerow(finalHeader)
  writer.writerows(finalPlanetData)