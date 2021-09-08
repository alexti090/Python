import statistics as st
import csv
import math

with open('./CSV-Data/std_dev.csv', 'r') as f:
  file = csv.reader(f)
  row = next(file)

vals = []
for r in row:
  vals.append(int(r))

mean = st.mean(vals)
list1 = []

for m in vals:
  list1.append((mean-m)**2)

sum = sum(list1)
standardDeviation = math.sqrt(sum/len(list1)-1)
print(standardDeviation)