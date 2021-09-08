import pandas as pd
import plotly_express as px

df = pd.read_csv('./CSV-Data/math-attempts.csv')
mean = df.groupby(['student_id', 'level'], as_index=False)['attempts'].mean()
graph = px.scatter(mean, x='student_id', y='level', size='attempts', color = 'attempts')
graph.show()