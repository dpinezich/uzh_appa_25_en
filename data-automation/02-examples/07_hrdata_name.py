import pandas


df = pandas.read_csv('06_hrdata.csv', index_col='Name')
print(df)