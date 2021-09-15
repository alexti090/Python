import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import pandas
import random

df = pandas.read_csv('./CSV-Data/math-scores.csv')
scores = df['Math_score'].tolist()

populationMean = st.mean(scores)
populationDeviation = st.stdev(scores)
print(populationMean, populationDeviation)

def experiment():
  samples = []
  for i in range(100):
    randIndex = random.randint(0, len(scores)-1)
    samples.append(scores[randIndex])
  sampleMean = st.mean(samples)
  return sampleMean

listOfSampleMean = []
for i in range(1000):
  sampleMean = experiment()
  listOfSampleMean.append(sampleMean)

sampleMeanDistribution = st.mean(listOfSampleMean)
sampleDeviation = st.stdev(listOfSampleMean)

print(sampleMeanDistribution, sampleDeviation)

graph = ff.create_distplot([listOfSampleMean], ['Sample Distribution'], show_hist=False)

firstDeviationStart, firstDeviationEnd = sampleMeanDistribution-sampleDeviation, sampleMeanDistribution+sampleDeviation
secondDeviationStart, secondDeviationEnd = sampleMeanDistribution-(sampleDeviation*2), sampleMeanDistribution+(sampleDeviation*2)
thirdDeviationStart, thirdDeviationEnd = sampleMeanDistribution-(sampleDeviation*3), sampleMeanDistribution+(sampleDeviation*3)

# Statisticaly studying the effect of first intervention
df1 = pandas.read_csv('./CSV-Data/intervention1.csv')
scores1 = df1['Math_score'].tolist()
mean1 = st.mean(scores1)

zscore1 = (mean1-sampleMeanDistribution)/sampleDeviation
print('Zscore1', zscore1)

""" graph.add_trace(go.Scatter(x=[sampleMeanDistribution, sampleMeanDistribution], y=[0, 0.2], mode='lines', name='Mean'))
graph.add_trace(go.Scatter(x=[mean1, mean1], y=[0, 0.2], mode='lines', name='Mean of Intervention 1'))
graph.add_trace(go.Scatter(x=[firstDeviationEnd, firstDeviationEnd], y=[0, 0.2], mode='lines', name='First Deviation End'))
graph.add_trace(go.Scatter(x=[secondDeviationEnd, secondDeviationEnd], y=[0, 0.2], mode='lines', name='Second Deviation End'))
graph.add_trace(go.Scatter(x=[thirdDeviationEnd, thirdDeviationEnd], y=[0, 0.2], mode='lines', name='Third Deviation End')) """
""" graph.show() """


# Statisticaly studying the effect of second intervention
df2 = pandas.read_csv('./CSV-Data/intervention2.csv')
scores2 = df2['Math_score'].tolist()
mean2 = st.mean(scores2)

zscore2 = (mean2-sampleMeanDistribution)/sampleDeviation
print('Zscore2', zscore2)

"""
graph.add_trace(go.Scatter(x=[sampleMeanDistribution, sampleMeanDistribution], y=[0, 0.2], mode='lines', name='Mean'))
graph.add_trace(go.Scatter(x=[mean2, mean2], y=[0, 0.2], mode='lines', name='Mean of Intervention 2'))
graph.add_trace(go.Scatter(x=[firstDeviationEnd, firstDeviationEnd], y=[0, 0.2], mode='lines', name='First Deviation End'))
graph.add_trace(go.Scatter(x=[secondDeviationEnd, secondDeviationEnd], y=[0, 0.2], mode='lines', name='Second Deviation End'))
graph.add_trace(go.Scatter(x=[thirdDeviationEnd, thirdDeviationEnd], y=[0, 0.2], mode='lines', name='Third Deviation End'))
graph.show() """

#Statisticaly studying the effect of third intervention
df3 = pandas.read_csv('./CSV-Data/intervention3.csv')
scores3 = df3['Math_score'].tolist()
mean3 = st.mean(scores3)

zscore3 = (mean3-sampleMeanDistribution)/sampleDeviation
print('Zscore3', zscore3)

"""
graph.add_trace(go.Scatter(x=[sampleMeanDistribution, sampleMeanDistribution], y=[0, 0.2], mode='lines', name='Mean'))
graph.add_trace(go.Scatter(x=[mean3, mean3], y=[0, 0.2], mode='lines', name='Mean of Intervention 3'))
graph.add_trace(go.Scatter(x=[firstDeviationEnd, firstDeviationEnd], y=[0, 0.2], mode='lines', name='First Deviation End'))
graph.add_trace(go.Scatter(x=[secondDeviationEnd, secondDeviationEnd], y=[0, 0.2], mode='lines', name='Second Deviation End'))
graph.add_trace(go.Scatter(x=[thirdDeviationEnd, thirdDeviationEnd], y=[0, 0.2], mode='lines', name='Third Deviation End'))
graph.show() """