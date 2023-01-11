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
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

def save_to_excel(df_in, excel_file, sheet_name, condition=True):
    df = df_in.copy()
    for col in df.columns:
        if df[col].dtype != bool:
            df[col] = df[col].fillna("").astype(str)

    excel_writer = pd.ExcelWriter(
      excel_file,
      engine='xlsxwriter',
      datetime_format='yyyy-mm-dd'
    )
    
    df.to_excel(
        excel_writer=excel_writer,
        sheet_name=sheet_name,
        index=False,
        freeze_panes=(1, 0),
    )
    
    # auto-adjust column width
    
    # apply conditional format
```
