import plotly.figure_factory as ff
import statistics as st
import random
import pandas

df = pandas.read_csv('./CSV-Data/medium_data.csv')
readLst = df['reading_time'].tolist()
popMean = st.mean(readLst)

def experiment():
  samples = []
  for i in range(30):
    index = random.randint(0, len(readLst)-1)
    samples.append(readLst[index])
  return st.mean(samples)

meansLst = []
for i in range(100):
  meansLst.append(experiment())
sampMean = st.mean(meansLst)

print('Population Mean:', popMean, 'and Sample Mean:', sampMean)

graph = ff.create_distplot([meansLst], ['Means List'], show_hist=False)
graph.show()