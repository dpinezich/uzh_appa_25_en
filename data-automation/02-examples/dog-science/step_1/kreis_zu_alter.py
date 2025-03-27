import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('../data/20200306_hundehalter.csv')
distribution_dict = {}
for index, row in df.iterrows():
    if distribution_dict.get(row["STADTKREIS"]):
        if distribution_dict[row["STADTKREIS"]].get(row["ALTER"]):
            distribution_dict[row["STADTKREIS"]][row["ALTER"]] += 1
        else:
            distribution_dict[row["STADTKREIS"]][row["ALTER"]] = 1
    else:
        distribution_dict[row["STADTKREIS"]] = {}
        distribution_dict[row["STADTKREIS"]][row["ALTER"]] = 1

age_groups = ['11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']
city_parts = list(range(1,13))

full_list = []
for key, value in enumerate(city_parts):
    intermediate_list = []
    for k,v in enumerate(age_groups):
        if distribution_dict[value].get(v):
            intermediate_list.append(distribution_dict[value][v])
    full_list.append(intermediate_list)


fig = go.Figure(data=go.Heatmap(
                   z=full_list,
                   x=age_groups,
                   y=city_parts,
                   hoverongaps = False,
                   colorscale='Viridis'))
fig.show()