## Timer Decorator
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, *args, "begins ...")
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(func.__name__, *args, "complete!")
        print("time use:", round(t1 - t0), "seconds\n")
        return result
    return wrapper
```

## Pretty Table
```python
from prettytable import PrettyTable

def pretty_table(df: pd.DataFrame):
    df = df.round(4)
    table = PrettyTable()
    table.field_names = df.columns
    table.align = 'r'
    for i in range(len(df)):
        table.add_row(df.iloc[i])
    return table
```

## iPython Auto Reload
```python
from IPython import get_ipython

ipy = get_ipython()
if ipy.__class__.__name__ == 'TerminalInteractiveShell':
    if 'autoreload' not in ipy.extension_manager.loaded:
        ipy.magic("load_ext autoreload")
        ipy.magic("autoreload 2")
```

## Get Progress Report
```python
from datetime import datetime
import time

def get_progress_report(status, timestamp, **kwargs):

    if status == 0:
        line1 = "  Process started  "
    elif status == 1:
        line1 = "  Complete!  "
    else:
        raise ValueError("status must be integer 0 or 1!")

    line2 = "  %s  " % datetime.strftime(timestamp, '%Y-%m-%d %H:%M:%S')
    prompt = "\n{:*^80}\n{:*^80}".format(line1, line2)

    for k, v in kwargs.items():
        prompt += "\n{:*^80}".format(f"  {k}: {v}  ")
    prompt += "\n"
    print(prompt)
    pass

# usage
start = time.perf_counter()
get_progress_report(0, start, **kwargs)

finish = time.perf_counter()
seconds_used = (finish - start).seconds
minutes_used = round(seconds_used / 60, 2)
get_progress_report(1, finish, minutes_used=minutes_used)
```

