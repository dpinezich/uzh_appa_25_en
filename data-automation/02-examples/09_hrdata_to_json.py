import pandas

df = pandas.read_csv('06_hrdata.csv',
                     index_col='Employee',
                     parse_dates=['Hired'],
                     header=0,
                     names=['Employee', 'Hired', 'Salary', 'Sick Days'])

df.to_json('09_hrdata_modified.json')
