import pandas as pd
import plotly.express as px

data = pd.read_csv('./CSV-Data/covid-data.csv')
graph = px.scatter(data, x='Date', y='Cases', color='Country')
graph.show()