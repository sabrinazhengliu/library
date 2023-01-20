## Excel Writer
```python
import string
import itertools
import pandas as pd
pd.options.mode.chained_assignment = None
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None

def save_to_excel(df_in, excel_file, sheet_name, condition=False, save=False):
    
    df = df_in.copy()
    for col in df.columns:
        

```
