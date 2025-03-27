import pandas as pd
import collections
import pygal

data = {}


def get_ownerdata(file, year: int) -> None:
    df = pd.read_csv(file)
    dog_owner_place_dict = collections.OrderedDict(sorted(df['STADTKREIS'].value_counts().items(), key=lambda x: x[0]))
    prepare_data(dog_owner_place_dict, year)


def prepare_data(data_dict: dict, year: int) -> None:
    data[year] = data_dict


#get_ownerdata('../data/history/20151001_hundehalter.csv', 2015)
get_ownerdata('../data/history/20160307_hundehalter.csv', 2016)
get_ownerdata('../data/history/20170308_hundehalter.csv', 2017)
get_ownerdata('../data/history/20180305_hundehalter.csv', 2018)
get_ownerdata('../data/history/20190304_hundehalter.csv', 2019)


xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Correlation over years (number dogs)'
for key, value in data.items():
    print(key)
    print(list(value.items()))
    xy_chart.add(str(key), list(value.items()))
xy_chart.render_to_png('correlation_number_dogs_chart.png')

