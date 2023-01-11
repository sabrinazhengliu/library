## Regular Usage
```python
import argparse
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--report_date', help='yyyy-mm-dd', default=date.today())
parser.add_argument('-p', '--prod', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true', default=False)
```
