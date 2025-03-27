
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

age_groups, age_count = [], []

df = pd.read_csv('../data/20200306_hundehalter.csv')

for i, count in df['ALTER'].value_counts().sort_values().items():
    age_groups.append(i)
    age_count.append(count)


plt.rcdefaults()
fig, ax = plt.subplots()

y_pos = np.arange(len(age_groups))
performance = age_count

ax.barh(y_pos, performance, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(age_groups)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Count')
ax.set_title('Dog Owner Age')

plt.show()
