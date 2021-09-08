from collections import Counter
import csv

with open('./CSV-Data/SOCR-HeightWeight.csv', 'r') as f:
  file = csv.reader(f)
  ls = list(file)
ls.pop(0)
ls.sort()

heights = []
sum = 0.0
for l in ls:
  sum = sum + float(l[1])
  heights.append(float(l[1]))
print('Mean', sum/float(len(ls)))

if len(heights)%2 == 0:
  val1 = heights[len(heights)//2]
  val2 = heights[len(heights)//2+1]
  print(val1, val2)
  print('Median', (val1+val2)/2)
elif len(heights)%2 != 0:
  print('Median', heights[len(heights)//2])

count = Counter(heights)
print(count)