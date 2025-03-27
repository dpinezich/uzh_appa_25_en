import pandas

df = pandas.read_excel(open('ch-bevoelkerung.xlsx', 'rb'),
              sheet_name='VZ RFP 1850', index_col=2, header=2)

# print(df)
# print(df.head())

# print(df.describe())
# print(df['Einwohnerinnen und Einwohner'])
# print(df['Einwohnerinnen und Einwohner']['Aeugst'])

