import pandas as pd
import plotly_express as px
import numpy as np
import time

df = pd.read_csv("./CSV-Data/Coffee-vs-sleep.csv")
graph = px.scatter(df, x="Coffee in ml", y="sleep in hours")
corr = np.corrcoef(df["Coffee in ml"].tolist(), df["sleep in hours"].tolist())
print("Correlation between cups of coffee drunk and hours slept (in one week) is: "+str(corr[0][1]))
time.sleep(3)
print("Starting scatter plot on given data... ")
time.sleep(2)
graph.show()