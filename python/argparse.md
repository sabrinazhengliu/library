## Regular Usage
```python
import argparse
from datetime import date

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--target_date', help='yyyy-mm-dd', default=date.today())
parser.add_argument('-p', '--prod', action='store_true')
parser.add_argument('-v', '--verbose', action='store_true', default=True)
args = parser.parse_args()


target_date = args.target_date
if args.verbose:
    print('ok')
```


## Using Configuration File
```python
import argparse

runtime_args = {
    '-d': [
        '--target-date',
        dict(
            help='yyyy-mm-dd'
        )
        
    ],
    '-p': [
        '--document',
        dict(
            action='store_true',
            help='if True, do this'
        )
    ],
    '-v': [
        '--verbose',
        dict(
            action='store_true',
            help='if True, do that',
            default=True
        )
    ],
}

from config import runtime_args

parser = argparse.ArgumentParser()
for arg, specs in runtime_args.items():
    parser.add_argument(arg, specs[0], **specs[1])
args = parser.parse_args()

```


## Add Args to Params
```python
from config import query_params
query_params.update(
  {k: v for k, v in args.__dict__.items() if type(v) != bool}
)
```
