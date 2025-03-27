import openpyxl

wb = openpyxl.load_workbook('ch-bevoelkerung.xlsx')
wb.sheetnames # The workbook's sheets' names.
['VZ RFP 1850', 'VZ RFP 1860', 'VZ RFP 1870']

sheet = wb['VZ RFP 1850'] # Get a sheet from the workbook.

type(sheet)
# <class 'openpyxl.worksheet.worksheet.Worksheet'>
print(sheet.title) # Get the sheet's title as a string.
print(sheet['C15'].value)
print(sheet['D15'].value)


for cell in sheet['C']:
   print(cell.value)