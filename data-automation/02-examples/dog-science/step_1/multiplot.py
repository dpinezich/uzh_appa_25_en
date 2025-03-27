import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/20200306_hundehalter.csv')
sns.set_theme(style="darkgrid")

df = df[df['STADTKREIS'] > 8 ]

sns.displot(
    df, x="ALTER", col="STADTKREIS", row="GESCHLECHT",
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
)

plt.show()
