## Pandas General
```python
import pandas as pd
pd.options.mode.chained_assignment = None
pd.set_option('display.width', 2000)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
```

## Pandas to Excel
```python
import string
import itertools
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

def _apply_font_size(excel_writer, sheet_name, dict_col_width)
    fmt = {'font_size': 9}
    font_size = excel_writer.book.add_format(fmt)
    for c in range(len(dict_col_width)):
        excel_writer.sheets[sheet_name].set_column(
            c, c, list(dict_col_width.values())[c], font_size
        )
    return

def _apply_bold_header(excel_writer, sheet_name):
    fmt = {'font_size': 9, 'bold': True}
    font_bold = excel_writer.book.add_format(fmt)
    excel_writer.sheets[sheet_name].set_row(0, None, font_bold)
    return

def _apply_conditional_format(excel_writer, cols: list):
    
    def _get_exel_cols():
        list1 = [x for x in string.ascii_uppercase]
        list2 = [''] + list1
        col_names = list(map(''.join, itertools.product(list2, list1)))
        return col_names

    cols = [cols.index(c) for c in cols]           # to integer index
    cols = [_get_excel_cols()[c] for c in cols]    # to column names
    cols = [f'{c}1:{c}50000' for c in cols]        # to column range

    red_col = {'bg_color': '#FFC7CE', 'font_color': '#9C0006'}
    red_fmt = excel_writer.book.add_format(red_col)
    red_formula = {'type': 'cell', 'criteria': '=', 'value': True, 'format': red_fmt}
    
    for col in cols:
        excel_writer.sheets[sheet_name].conditional_format(col, formula)
    return

def save_to_excel(df_in, excel_file, sheet_name, condition=True, save=False):

    df = df_in.copy()
    for col in df.columns:
        if df[col].dtype != bool:
            df[col] = df[col].fillna("").astype(str)

    global excel_writer
    if not 'excel_writer' in globals().keys():
        excel_writer = pd.ExcelWriter(
          excel_file, engine='xlsxwriter',datetime_format='yyyy-mm-dd'
        )

    df.to_excel(
        excel_writer=excel_writer,
        sheet_name=sheet_name,
        index=False,
        freeze_panes=(1, 0),
    )

    # pre-define column width
    dict_col_width = {}
    for col in df.columns:
        if col == 'abc':
            dict_col_width[col] = 20
        elif col in ['c1', 'c2', 'c3']:
            dict_col_width[col] = 15
        else:
            dict_col_width[col] = 10    # default column width

    _apply_font_size(excel_writer, sheet_name, dict_col_width)
    _apply_bold_header(excel_writer, sheet_name)
    if condition:
        _apply_conditional_format(excel_writer, df.columns.tolist())
   
    print(f"Output saved to worksheet {sheet_name}")
    if save:
        excel_writer.save()
        print(f"Excel docucument {excel_file} is finalized!")
```
