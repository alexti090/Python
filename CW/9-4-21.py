from os import stat
import pandas as pd
import statistics
import math

class1 = pd.read_csv('./CSV-Data/class1.csv')
class2 = pd.read_csv('./CSV-Data/class2.csv')

def stdDev(df):
  mean = statistics.mean(df['Marks'])
  list1 = []
  s = 0
  standardDeviation = 0
  for m in df['Marks']:
    list1.append((m-mean)**2)
  s = sum(list1)
  standardDeviation = math.sqrt(s/len(list1)-1)
  print(standardDeviation)

stdDev(class1)
stdDev(class2)