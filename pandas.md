## Pandas General
```python
import pandas as pd
pd.options.mode.chained_assignment = None
pd.set_option('display.width', 2000)
pd.set_option('display.max_colwidth', 200)
```

## Pandas to Excel
```python
import pandas.io.formats.excel
pandas.io.formats.excel.ExcelFormatter.header_style = None
```
