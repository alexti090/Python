from numpy import gradient
import plotly.figure_factory as ff
import pandas

df = pandas.read_csv('./CSV-Data/mobile-ratings.csv')
mean = df.groupby('Mobile Brand', as_index=False)['Avg Rating'].mean()
graph = ff.create_distplot([df['Avg Rating']], ['Avg. Ratings'])
graph.show()