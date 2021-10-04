import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars', flavor="bs4")[0]
df.drop(df.columns[[0, 2, 4, 7]], axis=1, inplace=True)

df.rename(columns={
  'Proper name': 'name',
  'Distance (ly)': 'distance',
  'Mass (M☉)': 'mass',
  'Radius (R☉)': 'radius'
}, inplace=True)

df.replace({'[1]':''}, inplace=True)
df.replace({'[2]':''}, inplace=True)
df.replace({'´':''}, inplace=True)

df.to_csv('./Stars/scraped-data.csv')