import csv

data=[]
with open('./data2.csv') as f:
  reader = csv.reader(f)
  for row in reader:
    data.append(row)

headers = data[0]
planetData = data[1:]
for datapoint in planetData:
  datapoint[2] = datapoint[2].lower()

planetData.sort(key=lambda planetData:planetData[2])

with open('./data2-sorted.csv', 'a+') as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(planetData)