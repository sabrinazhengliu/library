## Load Daily Batch
```python
from datetime import date, timedelta

def get_start_date(window_days, back_fill=False):
    if back_fill:
        return '1900-01-01'
    return str(date.today() - timedelta(days=window_days))


def load_daily_batch(sql_scripts, table_name, window_days, back_fill=False):
    start_date = get_start_date(window_days, back_fill)
    qry_file = f"{current_directory}/sql/{sql_scripts}.sql"
    with open(qry_file, 'r') as f:
        qry = f.read()
    qry = qry.format(start_date=start_date)
    
    create = f"""
    create or replace table "{table_name}" cluster by (country) as
    """
    detele = f"""
    delete from "{table_name}" where txn_date >= '{start_date}'
    """
    insert = f"""
    insert into "{table_name}"
    """
    kwargs = datebase_config.copy()
    kwargs.update(show=True)
    if back_fill:
        execute_in_database(create + qry, **kwargs)
    else:
        execute_in_database(delete, **kwargs)
        execute_in_database(insert + qry, **kwargs)
    """
```
