import plotly.figure_factory as ff
import statistics as st
import pandas
import random

df = pandas.read_csv('./CSV-Data/temperature.csv')
temp = df['average'].tolist()
mean1 = st.mean(temp)
stdev1 = st.stdev(temp)
graph1 = ff.create_distplot([temp], ['Temperatures'])

meanlist = []
for i in range(800):
  randPopulation = []
  for i in range(100):
    rand = random.randint(1, len(temp)-1)
    randPopulation.append(temp[rand])
  meanlist.append(st.mean(randPopulation))
""" graph2 = ff.create_distplot([meanlist], ['Temperatures'], show_hist=False)
graph2.show() """
print(st.stdev(meanlist), stdev1)