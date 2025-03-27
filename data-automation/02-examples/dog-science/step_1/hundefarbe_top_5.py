import pygal
import pandas as pd

df = pd.read_csv('../data/20200306_hundehalter.csv')
dog_color = df['HUNDEFARBE'].value_counts()[0:6] # slicing

pie_chart = pygal.Pie(inner_radius=.4)
pie_chart.title = 'Top 5 Dog fur color in Zurich 2020'

for color, count in dog_color.items():
    pie_chart.add(color, count)

pie_chart.render_in_browser()