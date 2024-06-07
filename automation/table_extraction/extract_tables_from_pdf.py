'''
import camelot

tables = camelot.read_pdf('files/foo.pdf', pages='1', flavor='lattice')
print(tables)

tables.export('files_results/foo.csv', f='csv', compress=True)
tables[0].to_csv('files_results/foo.csv')  # to a csv file
print(tables[0].df)  # to a df
'''

import camelot

tables = camelot.read_pdf('foo.pdf')

tables
<TableList n=1>

tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite

tables[0]
<Table shape=(7, 7)>

tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}

tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite

tables[0].df # get a pandas DataFrame!