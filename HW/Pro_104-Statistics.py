import csv

with open('./CSV-Data/SOCR-HeightWeight.csv', 'r') as f:
  file = csv.reader(f)
  ls = list(file)
ls.pop(0)
ls.sort()

weights = []

sum = 0.0
for l in ls:
  sum = sum + float(l[2])
  weights.append(float(l[2]))
print('\n'+'Mean (average) weight is =>', sum/float(len(ls)))

if len(weights)%2 != 0:
  print('Median', weights[len(weights)//2])
elif len(weights)%2 == 0:
  val1 = weights[len(weights)//2]
  val2 = weights[len(weights)//2+1]
  print('Median weight is =>', (val1+val2)/2)

ranges = {"75-85": 0, "85-95": 0, "95-105": 0, "105-115": 0, "115-125": 0,"125-135": 0, "135-145": 0, "145-155": 0, "155-165": 0, "165-175": 0}

for i in weights:
  if i > 165:
    ranges["165-175"] += 1
  elif i > 155:
    ranges["155-165"] += 1
  elif i > 145:
    ranges["145-155"] += 1
  elif i > 135:
    ranges["135-145"] += 1
  elif i > 125:
    ranges["125-135"] += 1
  elif i > 115:
    ranges["115-125"] += 1
  elif i > 105:
    ranges["105-115"] += 1
  elif i > 95:
    ranges["95-105"] += 1
  elif i > 85:
    ranges["85-95"] += 1
  elif i > 75:
    ranges["75-85"] += 1

mode = ''
high = 0
for key in ranges:
  if ranges[key] > high:
    high = ranges[key]
    mode = key
print("Mode (most common) weight is between =>", mode)