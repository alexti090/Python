import plotly.figure_factory as ff
import statistics as st
import pandas

df = pandas.read_csv('./CSV-Data/performance.csv')
data = df[['math score', 'reading score', 'writing score']]

math = data['math score'].tolist()
reading = data['reading score'].tolist()
writing = data['writing score'].tolist()
scores = []

for c in range(len(math)):
  scores.append(math[c]+reading[c]+writing[c])

mean = st.mean(scores)
median = st.median(scores)
mode = st.mode(scores)
stdev = st.stdev(scores)

def range(i):
  minRange = mean - (i*stdev)
  maxRange = mean + (i*stdev)
  scoresInRange=[]
  for s in scores:
    if s >= minRange and s <= maxRange:
      scoresInRange.append(s)
  percent = (len(scoresInRange)/len(scores))*100
  return percent

stdev1 = range(1)
stdev2 = range(2)
stdev3 = range(3)

print(mean, median, mode)
print(stdev, stdev1, stdev2, stdev3)

graph = ff.create_distplot([scores], ['Scores'])
graph.show()
