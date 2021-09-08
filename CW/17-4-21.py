import pandas as pd
import plotly_express as px
import numpy as np

""" df = pd.read_csv("./CSV-Data/Attendance-vs-marks.csv")
graph = px.scatter(df, x="Marks In Percentage", y="Days Present")
graph.show()
correlation = np.corrcoef(df["Marks In Percentage"].tolist(), df["Days Present"].tolist())
print(correlation) """

df = pd.read_csv("./CSV-Data/Coffee-vs-sleep.csv")
graph = px.scatter(df, x="Coffee in ml", y="sleep in hours")
corr = np.corrcoef(df["Coffee in ml"].tolist(), df["sleep in hours"].tolist())
print(corr)
graph.show()