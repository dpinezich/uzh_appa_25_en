from bokeh.plotting import figure, show
import pandas as pd
import collections

df = pd.read_csv('../data/20200306_hundehalter.csv')
dog_age = df['GEBURTSJAHR_HUND'].value_counts() # Fehler 11 / 18 beachten
dog_age_dict = {}
current_year = 2021
for i, count in dog_age.items():
    if len(str(i)) > 3:
        dog_age_dict[current_year-i] = count

dog_age_dict = collections.OrderedDict(sorted(dog_age_dict.items(), key=lambda x: x[0])) # 1971 erklären

x, y = [], []
for key, value in dog_age_dict.items():
    if key < 26: #die letzten 3 entfernen
        x.append(key)
        y.append(value)

# create a new plot with a title and axis labels
p = figure(title="Amount of dogs by age", x_axis_label="x", y_axis_label="y")

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Age count", line_width=2)

# show the results
show(p)