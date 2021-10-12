import pandas as pd

df = pd.read_csv('./api/stars-filtered.csv', index_col=0)

data = []
for row in df.itertuples():
  star = {
    "name": row.name,
    "distance": row.distance,
    "mass": row.mass,
    "radius": row.radius,
    "gravity": row.gravity
  }
  data.append(star)
