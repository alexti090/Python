import pandas as pd

df1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars', flavor="bs4")[0]
df1 = df1[['Proper name', 'Distance (ly)', 'Mass (M☉)', 'Radius (R☉)']]

df2 = pd.read_html('https://en.wikipedia.org/wiki/List_of_brown_dwarfs', flavor="bs4")[3]
df2 = df2[['Star', 'Distance (ly)', 'Mass(MJ)', 'Radius(RJ)']]

df1.rename(columns={
  'Proper name': 'name',
  'Distance (ly)': 'distance',
  'Mass (M☉)': 'mass',
  'Radius (R☉)': 'radius'
}, inplace=True)

df2.rename(columns={
  'Star': 'name',
  'Distance (ly)': 'distance',
  'Mass(MJ)': 'mass',
  'Radius(RJ)': 'radius'
}, inplace=True)

df1.to_csv('./Stars/data1.csv')
df2.to_csv('./Stars/data2.csv')