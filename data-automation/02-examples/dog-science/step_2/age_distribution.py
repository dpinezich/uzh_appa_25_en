import pandas as pd
import collections
import pygal

data = {}

def get_ownerdata(file, year: int) -> None:
    df = pd.read_csv(file)
    dog_owner_age_dict = collections.OrderedDict(sorted(df['ALTER'].value_counts().items(), key=lambda x: x[0]))
    prepare_data(dog_owner_age_dict, year)


def prepare_data(data_dict: dict, year: int) -> None:
    value_list = []
    for key, value in data_dict.items():
        value_list.append(value)
    data[year] = value_list


get_ownerdata('../data/history/20151001_hundehalter.csv', 2015)
get_ownerdata('../data/history/20160307_hundehalter.csv', 2016)
get_ownerdata('../data/history/20170308_hundehalter.csv', 2017)
get_ownerdata('../data/history/20180305_hundehalter.csv', 2018)
get_ownerdata('../data/history/20190304_hundehalter.csv', 2019)

age_groups = ['11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']


line_chart = pygal.Bar()
line_chart.title = 'Age groups dog owners'
line_chart.x_labels = age_groups
for k,v in data.items():
    line_chart.add(str(k), v)

line_chart.render_to_png('correlation_age_owner_chart.png')

