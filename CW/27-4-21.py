import plotly.figure_factory as ff
import statistics as st
import pandas as pd

df = pd.read_csv('./CSV-Data/height-weight-data.csv')

heights = df['Height(Inches)'].tolist()

mean = st.mean(heights)
stdev = st.stdev(heights)
rangeMin = mean-stdev
rangeMax = mean+stdev

lst1 = []
for h in heights:
  if h >= rangeMin and h <= rangeMax:
    lst1.append(h)

percent = (len(lst1)/len(heights))*100
print(percent)

rangeMin2 = mean - 2*stdev
rangeMax2 = mean + 2*stdev

lst2 = []
for h in heights:
  if h >= rangeMin2 and h <= rangeMax2:
    lst2.append(h)

percent2 = (len(lst2)/len(heights))*100
print(percent2)

rangeMin3 = mean - 3*stdev
rangeMax3 = mean + 3*stdev

lst3 = []
for h in heights:
  if h >= rangeMin3 and h <= rangeMax3:
    lst3.append(h)

percent3 = (len(lst3)/len(heights))*100
print(percent3)

""" weights = df['Weight(Pounds)'].tolist()

mean = st.mean(weights)
stdev = st.stdev(weights)
rangeMin = mean-stdev
rangeMax = mean+stdev

lst1 = []
for w in weights:
  if w >= rangeMin and w <= rangeMax:
    lst1.append(w)

percent = (len(lst1)/len(weights))*100
print(percent)

rangeMin2 = mean - 2*stdev
rangeMax2 = mean + 2*stdev

lst2 = []
for w in weights:
  if w >= rangeMin2 and w <= rangeMax2:
    lst2.append(w)

percent2 = (len(lst2)/len(weights))*100
print(percent2)

rangeMin3 = mean - 3*stdev
rangeMax3 = mean + 3*stdev

lst3 = []
for w in weights:
  if w >= rangeMin3 and w <= rangeMax3:
    lst3.append(w)

percent3 = (len(lst3)/len(weights))*100
print(percent3) """
