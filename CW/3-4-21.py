import pandas as pd
import plotly.express as px

data = pd.read_csv('c:/Users/harsh/Desktop/Python/data.csv')
fig = px.scatter(data, x = 'Country', y = 'Country', size = 'Percentage', color = 'Country')
fig.show()