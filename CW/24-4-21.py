import plotly.figure_factory as ff
import pandas
import random

df = pandas.read_csv('./CSV-Data/height-weight-data.csv')

sums = []
count = []

for i in range(1000):
  num1 = random.randint(1, 6)
  num2 = random.randint(1, 6)
  sums.append(num1 + num2)

fig = ff.create_distplot([sums], ['result'])
fig2 = ff.create_distplot([df['Height(Inches)']], ['Height'])
fig3 = ff.create_distplot([df['Weight(Pounds)']], ['Weight'])

fig3.show()