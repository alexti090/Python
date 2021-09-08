import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('./CSV-Data/math-attempts.csv')
student = df.loc[df['student_id'] == 'TRL_imb']
mean = student.groupby('level')['attempt'].mean()
graph = go.Figure(go.Bar(x=mean, y=['Level 1', 'Level 2', 'Level 3', 'Level 4'], orientation='h'))
graph.show()